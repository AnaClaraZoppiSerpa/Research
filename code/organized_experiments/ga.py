import galois
import math
import pprint

from matrix_evaluation import *

from initial_population_functions import *
from selection_functions import *
from pairing_functions import *
from reproduction_functions import *
from crossover_functions import *
from mutation_functions import *
from replacement_functions import *
from lookup import *

BASELINES = {
    8: 296,
    4: 40,
    3: 15,
    2: 8,
    5: 120,
    6: 234,
    7: 384,
    16: 4544,
    32: 20032,
}

GF2_4 = galois.GF(2 ** 4)
GF2_8 = galois.GF(2 ** 8)


class Arguments:
    def __init__(self, upper, replacement_num_elites, replacement_num_survivors, replacement_tournament_size,
                 pairing_tournament_size, initial_population_size, max_iterations, selection_num_parents,
                 mutation_prob):
        self.upper = upper
        self.num_elites = replacement_num_elites
        self.num_survivors = replacement_num_survivors
        self.tournament_size = replacement_tournament_size
        self.pairing_tournament_size = pairing_tournament_size
        self.initial_population_size = initial_population_size
        self.max_iterations = max_iterations
        self.selection_num_parents = selection_num_parents
        self.mutation_prob = mutation_prob


class ExperimentSettings:
    def __init__(self, order, dimension, field):
        self.order = order
        self.integer_upper_limit = 2 ** self.order - 1
        self.dimension = dimension
        self.field = field


class ChosenFunctions:
    def __init__(self, initialization_f, selection_f, pairing_f, crossover_f, mutation_f, replacement_f):
        self.initialization_f = initialization_f
        self.selection_f = selection_f
        self.pairing_f = pairing_f
        self.crossover_f = crossover_f
        self.mutation_f = mutation_f
        self.replacement_f = replacement_f

class Results:
    def __init__(self):
        self.discovered_mds_candidates = []
        self.already_existing_candidates = []
        self.discovered_mds_with_same_cost = []
        self.discovered_mds_with_better_cost = []
        self.mds_count = 0
        self.non_mds_count = 0

    def mds_discovery(self, candidate):
        self.discovered_mds_candidates.append(candidate)

    def repeated(self, candidate):
        self.already_existing_candidates.append(candidate)

    def mds_same_cost_discovery(self, candidate):
        self.discovered_mds_with_same_cost.append(candidate)

    def mds_better_cost_discovery(self, candidate):
        self.discovered_mds_with_better_cost.append(candidate)

    def count_mds(self):
        self.mds_count += 1

    def count_non_mds(self):
        self.non_mds_count += 1

    def print_compact(self):
        print("MDS count X non-mds count:", self.mds_count, "X", self.non_mds_count)
        print("MDS worse discovered:", len(self.discovered_mds_candidates))
        print("Repeated:", len(self.already_existing_candidates))
        print("MDS same:", len(self.discovered_mds_with_same_cost))
        print("MDS better:", len(self.discovered_mds_with_better_cost))

    def print_full(self):
        print("MDS count X non-mds count:", self.mds_count, "X", self.non_mds_count)
        print("MDS worse discovered:", len(self.discovered_mds_candidates))
        print("Repeated:", len(self.already_existing_candidates))
        print("MDS same:", len(self.discovered_mds_with_same_cost))
        print("MDS better:", len(self.discovered_mds_with_better_cost))

        # Imprimir quais foram as matrizes repetidas, se existirem
        # Imprimir as MDS piores
        # Imprimir as MDS melhores
        # Imprimir as MDS iguais

        print("The repeated matrices found were these:")
        for candidate in self.already_existing_candidates:
            print(candidate.dataset_id)

        print("The MDS matrices found were these:")
        for candidate in self.discovered_mds_candidates:
            print("cost =", candidate.cost, "baseline diff =", candidate.baseline_diff)
            print("dim", candidate.dim)
            print("xor", candidate.xor)
            print("xtime", candidate.xtime)
            print(candidate.matrix)

        print("The MDS matrices with same cost as baseline found were these:")
        for candidate in self.discovered_mds_with_same_cost:
            print("cost =", candidate.cost, "baseline diff =", candidate.baseline_diff)
            print("dim", candidate.dim)
            print("xor", candidate.xor)
            print("xtime", candidate.xtime)
            print(candidate.matrix)

        print("The MDS matrices with better cost found were these:")
        for candidate in self.discovered_mds_with_better_cost:
            print("cost =", candidate.cost, "baseline diff =", candidate.baseline_diff)
            print("dim", candidate.dim)
            print("xor", candidate.xor)
            print("xtime", candidate.xtime)
            print(candidate.matrix)


class Candidate:
    def __init__(self, matrix, mds, invertible, xor, xtime, inverse, dim):
        self.matrix = matrix
        self.mds = mds
        self.invertible = invertible
        self.xor = xor
        self.xtime = xtime
        self.inverse = inverse
        self.dim = dim
        self.cost = 3 * self.xtime + 1 * self.xor
        self.baseline_diff = self.cost - BASELINES[dim]

        if self.baseline_diff > 0:
            self.ranking = "WORSE"
        if self.baseline_diff == 0:
            self.ranking = "SAME"
        if self.baseline_diff < 0:
            self.ranking = "BETTER"

        self.already_exists = False
        self.dataset_id = ""

        lookup = exists_in_dataset(LOOKUP_DICT, self.matrix)
        if lookup[0]:
            self.already_exists = True
            self.dataset_id = lookup[1]

    def fitness(self):
        return -self.cost


def get_candidate_data(mat, field, poly_order):
    dim = len(mat)
    is_invertible = True
    alg_mat = int_to_gf_mat(mat, field)
    inv = None

    is_mds_mat = is_mds(alg_mat)
    mat_xor = matrix_xor_cost(alg_mat, poly_order)
    mat_xtime = matrix_xtime_cost(alg_mat, poly_order)

    try:
        inv = np.linalg.inv(alg_mat)
    except:
        is_invertible = False

    return Candidate(mat, is_mds_mat, is_invertible, mat_xor, mat_xtime, inv, dim)


def to_candidates(list_of_matrices, E):
    candidates = []
    for matrix in list_of_matrices:
        c = get_candidate_data(matrix, E.field, E.order)
        candidates.append(c)
    return candidates


def log(candidates, log_string):
    print(log_string)
    print("len =", len(candidates))
    for (i, candidate) in enumerate(candidates):
        print("candidate", i)
        print("fitness", candidate.fitness())
        print("ranking", candidate.ranking)
        print("diff", candidate.baseline_diff)
        print("exists?", candidate.already_exists)
        print("id", candidate.dataset_id)
        print("mds?", candidate.mds)
        print(candidate.matrix)

def result_storage(candidates, R):
    for (i, candidate) in enumerate(candidates):
        if candidate.mds:
           R.count_mds()
        else:
            R.count_non_mds()

        if candidate.already_exists:
            R.repeated(candidate)
        elif candidate.mds:
            if candidate.ranking == "SAME":
                R.mds_same_cost_discovery(candidate)
            elif candidate.ranking == "BETTER":
                R.mds_better_cost_discovery(candidate)
            else:
                R.mds_discovery(candidate)

def evolve(E, A, F):
    R_population = Results()
    R_offspring = Results()

    population = to_candidates(
        F.initialization_f(A.initial_population_size, E.integer_upper_limit, E.dimension, E.dimension, A), E)

    iteration_count = 0

    while iteration_count < A.max_iterations:
        print("ITERATION", iteration_count+1, "/", A.max_iterations)

        result_storage(population, R_population)
        log(population, "starting population, iteration:" + str(iteration_count))

        selected_parents = F.selection_f(population, A.selection_num_parents)
        parent_pairs = F.pairing_f(selected_parents, A)
        offspring = to_candidates(reproduction(parent_pairs, A.mutation_prob, F.crossover_f, F.mutation_f, A), E)

        result_storage(offspring, R_offspring)
        log(offspring, "offspring, iteration:" + str(iteration_count))

        population = F.replacement_f(population, offspring, A)

        iteration_count += 1

    print("Population analysis:")
    R_population.print_full()
    print("Offspring analysis:")
    R_offspring.print_full()

def test():
    E = ExperimentSettings(4, 3, GF2_4)
    A = Arguments(E.integer_upper_limit, 6, 6, 6, 3, 10, 400, 8, 0.1)
    F = ChosenFunctions(random_initialization,
                        selection1,
                        pairing1,
                        crossover1,
                        mutation1,
                        replacement1)
    evolve(E, A, F)

test()
