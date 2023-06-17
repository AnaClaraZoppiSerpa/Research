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

"""
dim = 8 mat count = 2 cost = 296
dim = 4 mat count = 2 cost = 40
dim = 3 mat count = 74 cost = 15
dim = 2 mat count = 2 cost = 8
dim = 5 mat count = 1 cost = 120
dim = 6 mat count = 1 cost = 234
dim = 7 mat count = 1 cost = 384
dim = 16 mat count = 1 cost = 4544
dim = 32 mat count = 1 cost = 20032
"""

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

# SETUP

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


def evolve(E, A, F):
    population = to_candidates(
        F.initialization_f(A.initial_population_size, E.integer_upper_limit, E.dimension, E.dimension, A), E)

    iteration_count = 0

    while iteration_count < A.max_iterations:
        selected_parents = F.selection_f(population, A.selection_num_parents)
        parent_pairs = F.pairing_f(selected_parents, A)
        offspring = to_candidates(reproduction(parent_pairs, A.mutation_prob, F.crossover_f, F.mutation_f, A), E)
        population = F.replacement_f(population, offspring, A)

        iteration_count += 1
        #print(iteration_count, "/", A.max_iterations)
    #print("OK")


E = ExperimentSettings(4, 3, GF2_4)
A = Arguments(E.integer_upper_limit, 6, 6, 6, 3, 10, 10, 8, 0.1)

combination = 0
for ini in [random_initialization]: # 1 * 5 * 5 * 6 * 4 * 4
    for se in [selection1, selection2, selection3, selection4, selection5]:
        for pa in [pairing1, pairing2, pairing3, pairing4, pairing5]:
            for cr in [crossover1, crossover2, crossover3, crossover4, crossover5, crossover6]:
                for mu in [mutation1, mutation2, mutation3, mutation4]:
                    for re in [replacement1, replacement2, replacement3, replacement4]:
                        combination += 1
                        F = ChosenFunctions(ini, se, pa, cr, mu, re)
                        try:
                            evolve(E, A, F)
                        except:
                            print("errored combination:", combination)
                            print(ini, se, pa, cr, mu, re)
                            continue
                        else:
                            print("ok combination: ", combination)
