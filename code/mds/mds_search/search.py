import itertools
import numpy as np
import galois
import math
import sys
import argparse
import datetime
from baselines import *

# Configurações
GF2 = galois.GF(2)
rijndael_poly = galois.Poly([1, 0, 0, 0, 1, 1, 0, 1, 1], field=GF2)
debug = True
experiment_id = ""

# Funções auxiliares

# Funções pra calcular custos de matriz
def poly_xtime_cost(poly, ORDER):
    if poly == 0:
       return 0
    degree = ORDER
    degree_mask = 2**ORDER

    while (poly & degree_mask) == 0:
        degree_mask = degree_mask >> 1
        degree -= 1
    return degree

def poly_xor_cost(poly, ORDER):
    mask = 1
    set_bits = 0
    current_bit = 0
    while current_bit < ORDER:
        if (poly & mask) != 0:
            set_bits += 1
        mask = mask << 1
        current_bit += 1
    return set_bits - 1

def matrix_xtime_cost(mat, ORDER):
    total_cost = 0
    for row in range(len(mat)):
        row_cost = 0
        for col in range(len(mat[row])):
            row_cost += poly_xtime_cost(mat[row][col], ORDER)
        total_cost += row_cost
    return total_cost

def matrix_xor_cost(mat, ORDER):
    total_cost = 0
    for row in range(len(mat)):
        row_cost = len(mat) - 1
        for col in range(len(mat[row])):
            row_cost += poly_xor_cost(mat[row][col], ORDER)
        total_cost += row_cost
    return total_cost

# Converter um inteiro pra um polinômio do pacote Galois
def int_to_gf(int_poly):
    coeffs = []
    for x in bin(int_poly)[2:]:
        coeffs.append(int(x))

    return galois.Poly(coeffs, field=GF2)

# Converter uma matriz de inteiros pra uma matriz com elementos de um corpo finito
def int_to_gf_mat(int_mat, field):
    rows = len(int_mat)
    cols = len(int_mat[0])

    gf_mat = field.Zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            gf_mat[i][j] = int_mat[i][j]

    return gf_mat

# Ver se uma matriz é MDS, sendo essa matriz uma matriz com elementos de corpos finitos
def is_mds(mat_in_field):
	if np.linalg.det(mat_in_field) == 0:
		return False

	dim = len(mat_in_field)

	dim_list = [i for i in range(dim)]

	z = 1
	while z < dim:
		possibilities = list(itertools.combinations(dim_list, z))

		for rows_to_be_removed in possibilities:
			for columns_to_be_removed in possibilities:
				submat = np.delete(mat_in_field, rows_to_be_removed, axis=0)
				submat = np.delete(submat, columns_to_be_removed, axis=1)
				if np.linalg.det(submat) == 0:
					return False
		z += 1
	return True

# Funções principais

# Função pra gerar todos os vetores de um certo tamanho dado um conjunto de coeficientes que podem ser usados
def generate_arrays(element_set, array_length):
    arrs = itertools.product(element_set, repeat=array_length)
    return arrs

def print_mat_hex(m):
    for i in range(len(m)):
        row = []
        for j in range(len(m)):
            row.append(hex(m[i][j]))
        print(row)

def print_matrix_in_all_forms(matrix, field, upper_bound, poly):
    print("Polynomial representation")
    with field.display("poly"):
        print(matrix)

    print("Integer representation")
    print(matrix)

    print("Hexadecimal representation")
    print_mat_hex(matrix)

    max_degree = poly.degree

    print("XOR cost:", matrix_xor_cost(matrix, max_degree))
    print("XTIME cost:", matrix_xtime_cost(matrix, max_degree))

def save_matrix_data_gf256_rijndael_poly(matrix, inverse):
    xor_enc = matrix_xor_cost(matrix, 8)
    xtime_enc = matrix_xtime_cost(matrix, 8)
    xor_dec = matrix_xor_cost(inverse, 8)
    xtime_dec = matrix_xtime_cost(inverse, 8)
    xor_sum = xor_enc + xor_dec
    xtime_sum = xtime_enc + xtime_dec

    timestamp = str(datetime.datetime.now())
    f = open(experiment_id+timestamp, "w")

    f.write("xor_enc: " + str(xor_enc) + "\n")
    f.write("xtime_enc: " + str(xtime_enc) + "\n")

    f.write("=========\n")

    f.write("xor_dec: " + str(xor_dec) + "\n")
    f.write("xtime_dec: " + str(xtime_dec) + "\n")

    f.write("=========\n")

    f.write("xor_sum: " + str(xor_sum) + "\n")
    f.write("xtime_sum: " + str(xtime_sum) + "\n")

    f.write("mat:\n")
    f.write(str(matrix))
    f.write("\ninv:\n")
    f.write(str(inverse))

    log = compare_to_baselines(xor_enc, xtime_enc, xor_dec, xtime_dec, xor_sum, xtime_sum)
    f.write(log)

    return {
        "xor_enc": xor_enc,
        "xtime_enc": xtime_enc,
        "xor_dec": xor_dec,
        "xtime_dec": xtime_dec,
        "xor_sum": xor_sum,
        "xtime_sum": xtime_sum,
    }

    f.close()

# Avaliar se uma matriz é MDS dado o corpo finito (o limite - 2**8, 2**4, etc - e o polinômio irredutível)
def is_mds_for_field_returning_data(integer_matrix, upper_bound, poly):
    field = galois.GF(upper_bound, irreducible_poly=poly)
    matrix = int_to_gf_mat(integer_matrix, field)
    is_ = is_mds(matrix)

    data = {
        "xor_enc": math.inf,
        "xtime_enc": math.inf,
        "xor_dec": math.inf,
        "xtime_dec": math.inf,
        "xor_sum": math.inf,
        "xtime_sum": math.inf,
    }

    if is_:
        inverse = np.linalg.inv(matrix)
        assert(is_mds(inverse))
        data = save_matrix_data_gf256_rijndael_poly(matrix, inverse)

    return {
        "is_mds": is_,
        "data": data,
    }

# Avaliar se uma matriz é MDS dado o corpo finito (o limite - 2**8, 2**4, etc - e o polinômio irredutível)
def is_mds_for_field(integer_matrix, upper_bound, poly):
    field = galois.GF(upper_bound, irreducible_poly=poly)
    matrix = int_to_gf_mat(integer_matrix, field)
    is_ = is_mds(matrix)

    if is_:
        print("Found MDS matrix for GF", upper_bound ,"and p(x) =", poly)
        print_matrix_in_all_forms(matrix, field, upper_bound, poly)
        inverse = np.linalg.inv(matrix)
        print("Inverse matrix:")
        print_matrix_in_all_forms(inverse, field, upper_bound, poly)
        assert(is_mds(inverse))
        print("which is also MDS.")

        save_matrix_data_gf256_rijndael_poly(matrix, inverse)

    return is_

def array_to_generic_matrix(array):
    n = int(math.sqrt(len(array)))
    assert(n*n == len(array))

    mat = [[1 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            mat[i][j] = array[i*n+j]
    return mat

def array_to_right_circulant_matrix(array):
    first_row = list(array)
    dim = len(first_row)

    rows = []
    prev_row = []

    for i in range(dim):
        if i == 0:
            rows.append(first_row)
            prev_row = first_row
        else:
            new_first = prev_row[-1]
            new_row = [new_first]
            new_row += prev_row[0:-1]
            rows.append(new_row)
            prev_row = new_row
    return rows

def array_to_left_circulant_matrix(array):
    first_row = list(array)
    dim = len(first_row)

    rows = []
    prev_row = []

    for i in range(dim):
        if i == 0:
            rows.append(first_row)
            prev_row = first_row
        else:
            new_row = prev_row[1:]
            new_last = prev_row[0]
            new_row += [new_last]
            rows.append(new_row)
            prev_row = new_row
    return rows

def array_to_hadamard_matrix(array):
    n = len(array)

    mat = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            xor = i ^ j
            mat[i][j] = array[xor]

def array_to_vandermonde_matrix(array):
    print("Array to Vandermonde - Not yet implemented!")
    assert(1 == 0)

def array_to_cauchy_matrix(array):
    print("Array to Cauchy - Not yet implemented!")
    assert(1 == 0)

def array_to_serial_matrix(array):
    print("Array to Serial - Not yet implemented!")
    assert(1 == 0)

def array_to_hadamard_cauchy_matrix(array):
    print("Array to Hadamard Cauchy - Not yet implemented!")
    assert(1 == 0)

def array_to_compact_cauchy_matrix(array):
    print("Array to Compact Cauchy - Not yet implemented!")
    assert(1 == 0)

def get_arrays(element_set_uper_bound, length):
    element_set = [i for i in range(1, element_set_uper_bound)]
    return generate_arrays(element_set, length)

def look_for_mds(coefficient_upper_bound, array_length, field_upper_bound, field_poly, type):
    arrays = get_arrays(coefficient_upper_bound, array_length)
    for array in arrays:
        if debug:
            print(array)

        if type == 'right_circulant':
            equivalent_matrix = array_to_right_circulant_matrix(array)
        elif type == 'left_circulant':
            equivalent_matrix = array_to_left_circulant_matrix(array)
        elif type == 'generic':
            equivalent_matrix = array_to_generic_matrix(array)

        is_mds_for_field(equivalent_matrix, field_upper_bound, field_poly)

def gf256_rijndael_poly_experiment(last_coeff, matrix_dim, type):
    array_length = matrix_dim
    look_for_mds(last_coeff+1, array_length, 2**8, rijndael_poly, type)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--last_coeff', help='Last valid coefficient for the MDS matrix.')
    parser.add_argument('--dim', help='MDS matrix dimensions.')
    parser.add_argument('--type', help='Matrix type to search: right_circulant, left_circulant, generic.')
    parser.add_argument('--exp_id', help='Identifier for the experiment output.')

    args = parser.parse_args()
    last_coeff = int(args.last_coeff)
    dim = int(args.dim)
    type = str(args.type)
    experiment_id = args.exp_id

    gf256_rijndael_poly_experiment(last_coeff, dim, type)
