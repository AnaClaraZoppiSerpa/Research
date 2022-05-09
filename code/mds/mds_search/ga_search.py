# Configurações
# Polinômio: Rijndael
# Corpo: GF(2^8)
# Dimensões: fixar.
# Baselines para bater e reportar que bateu

import random
import galois
import math
import pprint
from search import is_mds_for_field_returning_data
from aux import get5x5array_1, get5x5array_2, get5x5array_3, get5x5array_4

settings_upper_bound = 16 #256 for GF(2^8) #16 for GF(2^4)
GF2 = galois.GF(2)
rijndael_poly = galois.Poly([1, 0, 0, 0, 1, 1, 0, 1, 1], field=GF2)
photon_poly = galois.Poly.Degrees([4, 1, 0], field=GF2)
settings_poly = photon_poly

settings_max_iterations = 1000
crossover_type = "random" # alternating | midpoint | random
mutation_type = "random_replace_by_random"
# random_decrease | random_replace_by_random | largest_decrease | largest_replace_by_one | largest_replace_by_random
selection_type = "randomly" # randomly | most_fit
replacement_type = "most_fit" # most_fit | random | only_new
mutation_rate = 0.9 # between 0 and 1

last_field_element = 15 # 255 for GF(2^8) # 15 for GF(2^4)

# Fitness settings - change according to optimization priority
weights = {
    'xtime': -0.5,
    'xor': -0.5,
    'xtime_inv': -0.0,
    'xor_inv': -0.0,
    'xtime_sum': -2.0,
    'xor_sum': -1.0,
}

def vector_to_matrix(vector):
    n = int(math.sqrt(len(vector)))
    assert(n*n == len(vector))

    mat = [[1 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            mat[i][j] = vector[i*n+j]
    return mat

def compute_fitness(chr):
    if chr['mds'] == False:
        return -math.inf

    return (chr['xtime']*weights['xtime']
    + chr['xor']*weights['xor']
    + chr['xtime_inv']*weights['xtime_inv']
    + chr['xor_inv']*weights['xor_inv']
    + chr['xtime_sum']*weights['xtime_sum']
    + chr['xor_sum']*weights['xor_sum'])

def get_vector_dict(vector):
    mat = vector_to_matrix(vector)
    data = is_mds_for_field_returning_data(mat, settings_upper_bound, settings_poly)

    d = {
        "vector": vector,
        "matrix": mat,
        "xor": data['data']['xor_enc'],
        "xtime": data['data']['xtime_enc'],
        "xtime_inv": data['data']['xtime_dec'],
        "xor_inv": data['data']['xor_dec'],
        "xor_sum": data['data']['xor_sum'],
        "xtime_sum": data['data']['xtime_sum'],
        "fitness": 0,
        "mds": data['is_mds']
    }

    d['fitness'] = compute_fitness(d)

    return d

def crossover_midpoint(chr_a, chr_b):
    a = chr_a['vector']
    b = chr_b['vector']

    assert(len(a) == len(b))
    size = len(a)

    midpoint = size//2

    child1 = []
    child2 = []

    index = 0
    while index < size:
        if index < midpoint:
            child1.append(a[index])
            child2.append(b[index])
        else:
            child1.append(b[index])
            child2.append(a[index])
        index+=1

    return [child1, child2]

def crossover_alternating(chr_a, chr_b):
    a = chr_a['vector']
    b = chr_b['vector']

    assert(len(a) == len(b))
    size = len(a)

    child1 = []
    child2 = []

    index = 0
    while index < size:
        if index % 2 == 0:
            child1.append(a[index])
            child2.append(b[index])
        else:
            child1.append(b[index])
            child2.append(a[index])
        index+=1

    return [child1, child2]

def crossover_random(chr_a, chr_b):
    a = chr_a['vector']
    b = chr_b['vector']

    assert(len(a) == len(b))
    size = len(a)

    midpoint = random.randint(0, size-1)

    child1 = []
    child2 = []

    index = 0
    while index < size:
        if index < midpoint:
            child1.append(a[index])
            child2.append(b[index])
        else:
            child1.append(b[index])
            child2.append(a[index])
        index+=1

    return [child1, child2]

def mutation_random_decrease(x):
    size = len(x)
    mutation_point = random.randint(0, size-1)
    x[mutation_point] = max(1, x[mutation_point]-1)

    return x

def mutation_random_replace_by_random(x):
    size = len(x)
    mutation_point = random.randint(0, size-1)
    x[mutation_point] = random.randint(1, last_field_element)

    return x

def mutation_largest_decrease(x):
    size = len(x)
    index = 0
    max_index = 0
    max_element = 0

    while index < size:
        if max_element < x[index]:
            max_index = index
            max_element = x[index]
        index+=1

    x[max_index] = max(1, x[max_index]-1)
    return x

def mutation_largest_replace_by_one(x):
    size = len(x)
    index = 0
    max_index = 0
    max_element = 0

    while index < size:
        if max_element < x[index]:
            max_index = index
            max_element = x[index]
        index+=1

    x[max_index] = 1
    return x

def mutation_largest_replace_by_random(x):
    size = len(x)
    index = 0
    max_index = 0
    max_element = 0

    while index < size:
        if max_element < x[index]:
            max_index = index
            max_element = x[index]
        index+=1

    x[max_index] = random.randint(1, last_field_element)
    return x

def select_to_reproduce_randomly(q, population):
    selected = []
    for i in range(q):
        choice = random.randint(0, len(population)-1)
        selected.append(population[choice])
    return selected

def select_to_reproduce_most_fit(q, population):
    sorted_population = sorted(population, key = lambda d: d['fitness'], reverse = True)
    return sorted_population[0:q]

def select_to_reproduce(q, population):
    if selection_type == "randomly":
        return select_to_reproduce_randomly(q, population)
    elif selection_type == "most_fit":
        return select_to_reproduce_most_fit(q, population)

def crossover(a, b):
    if crossover_type == "alternating":
        return crossover_alternating(a, b)
    elif crossover_type == "midpoint":
        return crossover_midpoint(a, b)
    elif crossover_type == "random":
        return crossover_random(a, b)

def mutate(x):
    z = random.random()

    if (z < mutation_rate):
        if mutation_type == "random_decrease":
            return mutation_random_decrease(x)
        elif mutation_type == "random_replace_by_random":
            return mutation_random_replace_by_random(x)
        elif mutation_type == "largest_decrease":
            return mutation_largest_decrease(x)
        elif mutation_type == "largest_replace_by_one":
            return mutation_largest_replace_by_one(x)
        elif mutation_type == "largest_replace_by_random":
            return mutation_largest_replace_by_random(x)
    return x

def reproduce(parents):
    parent1 = 0
    parent2 = parent1 + 1
    size = len(parents)

    all_children = []

    while (parent1 < size and parent2 < size):
        children = crossover(parents[parent1], parents[parent2])

        child1 = mutate(children[0])
        child2 = mutate(children[1])

        all_children += [child1, child2]
        parent1 += 2
        parent2 = parent1 + 1

    dict_children = []

    for c in all_children:
        dict_children.append(get_vector_dict(c))

    return dict_children

def replacement_most_fit(population, new_children, new_size):
    sorted_population = sorted(population+new_children, key = lambda d: d['fitness'], reverse = True)
    return sorted_population[0:new_size]

def replacement_random(population, new_children, new_size):
    everyone = population + new_children
    selected = []
    for i in range(new_size):
        choice = random.randint(0, len(everyone)-1)
        selected.append(everyone[choice])
    return selected

def replacement_only_new(population, new_children, new_size):
    return new_children

def replace_population(population, new_children, new_size):
    if replacement_type == "most_fit":
        return replacement_most_fit(population, new_children, new_size)
    elif replacement_type == "random":
        return replacement_random(population, new_children, new_size)
    elif replacement_type == "only_new":
        return replacement_only_new(population, new_children, new_size)

def initial_population():
    ini1 = get_vector_dict(get5x5array_1())
    ini2 = get_vector_dict(get5x5array_2())
    ini3 = get_vector_dict(get5x5array_3())
    ini4 = get_vector_dict(get5x5array_4())

    return [ini1, ini2, ini3, ini4]

def filter_for_mds(elements):
    only_mds_elements = []
    for c in elements:
        if c['mds']:
            only_mds_elements.append(c)
    return only_mds_elements

def get_population_stats(population):
    # Best individual and best fitness
    best_x = {}
    best_fitness = -math.inf
    for x in population:
        if x['fitness'] > best_fitness:
            best_fitness = x['fitness']
            best_x = x

    # Worst individual and worst fitness
    worst_x = {}
    worst_fitness = math.inf
    for x in population:
        if x['fitness'] < worst_fitness:
            worst_fitness = x['fitness']
            worst_x = x

    # Average fitness
    fitness_sum = 0.0
    for x in population:
        fitness_sum += x['fitness']

    fitness_avg = fitness_sum / len(population)

    return {
        "best_x": best_x,
        "worst_x": worst_x,
        "avg_fitness": fitness_avg
    }


def evolution():
    population = filter_for_mds(initial_population())

    iterations = 0

    stats = {}

    while (iterations < settings_max_iterations and len(population) > 1):
        stats = get_population_stats(population)
        print("GA stats: best fitness =", stats['best_x']['fitness'], "worst fitness =", stats['worst_x']['fitness'], "avg fitness =", stats['avg_fitness'])

        parents = select_to_reproduce(4, population)
        new_children = reproduce(parents)
        only_mds = filter_for_mds(new_children)
        population = replace_population(population, only_mds, 4)

        print("GA log: iteration =", str(iterations) + "/" + str(settings_max_iterations), "children:", len(new_children), "MDS children:", len(only_mds), "new population size:", len(population))

        iterations += 1

    print("GA ended! Best individual:")
    pprint.pprint(stats['best_x'])

evolution()
