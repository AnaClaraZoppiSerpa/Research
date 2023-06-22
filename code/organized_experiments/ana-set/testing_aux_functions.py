from mutation_functions import *
from crossover_functions import *
import pprint

mat1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

mat2 = [
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18],
]

for crossover_f in [crossover1, crossover2, crossover3, crossover4, crossover5, crossover6]:
    children = crossover_f(mat1, mat2)
    print(crossover_f)
    print(children[0])
    print(children[1])