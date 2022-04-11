# Configurações
# Polinômio: Rijndael
# Corpo: GF(2^8)
# Dimensões: fixar.
# Baselines para bater e reportar que bateu

import random

crossover_type = ""
mutation_type = ""
selection_type = ""
replacement_type = ""
population_size = 0
selection_size = 0
mutation_rate = 0
select_q = 0

last_field_element = 255
population = []

chromossome = {
    "vector": None,
    "matrix": None,
    "xor": None,
    "xtime": None,
    "xtime_inv": None,
    "xor_inv": None,
    "xor_sum": None,
    "xtime_sum": None,
    "fitness:" None
}

def crossover_midpoint(a, b):
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

def crossover_alternating(a, b):
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

def crossover_random(a,b):
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

def select_to_reproduce_randomly(q):
    selected = []
    for i in range(q):
        choice = random.randint(0, len(population)-1)
        selected.append(population[choice])
    return selected

def select_to_reproduce_most_fit(q):
    sorted_population = sorted(population, key = lambda d: d['fitness'], reverse = True)
    return sorted_population[0:q]

def select_to_reproduce(q):
    if selection_type == "randomly":
        return select_to_reproduce_randomly(q)
    elif selection_type == "most_fit":
        return select_to_reproduce_most_fit(q)

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
        parent1 += 1
        parent2 = parent1 + 1

    return all_children

def replace_population(new_children):
    pass

def initial_population():
    pass

def evolution():
    population = initial_population()
    parents = select_to_reproduce(select_q)
    new_children = reproduce(parents)
