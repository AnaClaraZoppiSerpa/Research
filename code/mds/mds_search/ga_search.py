# Configurações
# Polinômio: Rijndael
# Corpo: GF(2^8)
# Dimensões: fixar.
# Baselines para bater e reportar que bateu

import random

def crossover_midpoint(a, b):
    assert(len(a) == len(b))
    size = len(a)

    midpoint = size//2

    child1 = []
    child2 = []

    index = 0
    while index < size:
        if index <= midpoint:
            child1.append(a[index])
            child2.append(b[index])
        else:
            child1.append(b[index])
            child2.append(a[index])

    return [child1, child2]

#def crossover_alternating(a, b):
#    pass

#def crossover_random(a,b):
#    pass
