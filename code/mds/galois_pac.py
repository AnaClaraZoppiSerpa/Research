import galois
import numpy as np
import pandas as pd
import pprint
import csv
import itertools

DEGREE_LIMIT_MASK = 0b10000 # 0x100 for order=8
ORDER = 4

GF2 = galois.GF(2)

shark_square_bksq_poly = galois.Poly([1, 1, 1, 1, 1, 0, 1, 0, 1], field=GF2)
tavares_khazad_anubis_poly = galois.Poly([1, 0, 0, 0, 1, 1, 1, 0, 1], field=GF2)
rijndael_poly = galois.Poly([1, 0, 0, 0, 1, 1, 0, 1, 1], field=GF2)
hierocrypt_poly = galois.Poly([1, 0, 1, 1, 0, 0, 0, 1, 1], field=GF2)
curupira_poly = galois.Poly([1, 0, 1, 0, 0, 1, 1, 0, 1], field=GF2)
fox_poly = galois.Poly.Degrees([8,7,6,5,4,3,0])
whirlwind_poly = galois.Poly.Degrees([4, 1, 0], field=GF2)

shark_field = galois.GF(2**8, irreducible_poly=shark_square_bksq_poly)
anubis_field = galois.GF(2**8, irreducible_poly=tavares_khazad_anubis_poly)
rijndael_field = galois.GF(2**8, irreducible_poly=rijndael_poly)
hierocrypt_field = galois.GF(2**8, irreducible_poly=hierocrypt_poly)
hierocrypt_higher_field = galois.GF(2**4)
curupira_field = galois.GF(2**8, irreducible_poly=curupira_poly)
grostl_field = galois.GF(2**8, irreducible_poly=rijndael_poly) # Grostl uses the same poly!
fox_field = galois.GF(2**8, irreducible_poly=fox_poly)
whirlpool_field = galois.GF(2**8, irreducible_poly=tavares_khazad_anubis_poly)

led_poly = galois.Poly.Degrees([4, 1, 0], field=GF2)
led_field = galois.GF(2**4, irreducible_poly=led_poly)

photon4cells_poly = galois.Poly.Degrees([4, 1, 0], field=GF2)
photon4cells_field = galois.GF(2**4, irreducible_poly=led_poly)

photon8cells_poly = rijndael_poly
photon8cells_field = rijndael_field

hiero_16x16 = [
	[1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
	[1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
	[1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
	[0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0],
	[1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
	[0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
	[0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
	[1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
	[1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
	[1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
	[1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
	[1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
	[1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
	[1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
	[1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0],
	[0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1]
]

hiero_8x8 = [
	[1, 0, 1, 0, 1, 1, 1, 0],
	[1, 1, 0, 1, 1, 1, 1, 1],
	[1, 1, 1, 0, 0, 1, 1, 1],
	[0, 1, 0, 1, 1, 1, 0, 1],
	[1, 1, 0, 1, 0, 1, 0, 1],
	[1, 1, 1, 0, 1, 0, 1, 0],
	[1, 1, 1, 1, 1, 1, 0, 1],
	[1, 0, 1, 0, 1, 0, 1, 1]
]

shark_mat = [
		[0xce, 0x95, 0x57, 0x82, 0x8a, 0x19, 0xb0, 0x01],
		[0xe7, 0xfe, 0x05, 0xd2, 0x52, 0xc1, 0x88, 0xf1],
		[0xb9, 0xda, 0x4d, 0xd1, 0x9e, 0x17, 0x83, 0x86],
		[0xd0, 0x9d, 0x26, 0x2c, 0x5d, 0x9f, 0x6d, 0x75],
		[0x52, 0xa9, 0x07, 0x6c, 0xb9, 0x8f, 0x70, 0x17],
		[0x87, 0x28, 0x3a, 0x5a, 0xf4, 0x33, 0x0b, 0x6c],
		[0x74, 0x51, 0x15, 0xcf, 0x09, 0xa4, 0x62, 0x09],
		[0x0b, 0x31, 0x7f, 0x86, 0xbe, 0x05, 0x83, 0x34]
	]

square_mat = [
		[0x02, 0x01, 0x01, 0x03],
		[0x03, 0x02, 0x01, 0x01],
		[0x01, 0x03, 0x02, 0x01],
		[0x01, 0x01, 0x03, 0x02]
	]

bksq_mat = [
    [3, 2, 2],
    [2, 3, 2],
    [2, 2, 3]
]

testmat = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

tavares_mat = [
    [0x93, 0x13, 0x57, 0xda, 0x58, 0x47, 0x0c, 0x1f],
    [0x13, 0x93, 0xda, 0x57, 0x47, 0x58, 0x1f, 0x0c],
    [0x57, 0xda, 0x93, 0x13, 0x0c, 0x1f, 0x58, 0x47],
    [0xda, 0x57, 0x13, 0x93, 0x1f, 0x0c, 0x47, 0x58],
    [0x58, 0x47, 0x0c, 0x1f, 0x93, 0x13, 0x57, 0xda],
    [0x47, 0x58, 0x1f, 0x0c, 0x13, 0x93, 0xda, 0x57],
    [0x0c, 0x1f, 0x58, 0x47, 0x57, 0xda, 0x93, 0x13],
    [0x1f, 0x0c, 0x47, 0x58, 0xda, 0x57, 0x13, 0x93]
]

khazad_mat = [
    [0x01, 0x03, 0x04, 0x05, 0x06, 0x08, 0x0b, 0x07],
    [0x03, 0x01, 0x05, 0x04, 0x08, 0x06, 0x07, 0x0b],
    [0x04, 0x05, 0x01, 0x03, 0x0b, 0x07, 0x06, 0x08],
    [0x05, 0x04, 0x03, 0x01, 0x07, 0x0b, 0x08, 0x06],
    [0x06, 0x08, 0x0b, 0x07, 0x01, 0x03, 0x04, 0x05],
    [0x08, 0x06, 0x07, 0x0b, 0x03, 0x01, 0x05, 0x04],
    [0x0b, 0x07, 0x06, 0x08, 0x04, 0x05, 0x01, 0x03],
    [0x07, 0x0b, 0x08, 0x06, 0x05, 0x04, 0x03, 0x01]
]

anubis_mat = [
    [0x01, 0x02, 0x04, 0x06],
    [0x02, 0x01, 0x06, 0x04],
    [0x04, 0x06, 0x01, 0x02],
    [0x06, 0x04, 0x02, 0x01]
]

anubis_ke_mat = [
    [0x01, 0x01, 0x01, 0x01],
    [0x01, 0x02, 0x04, 0x08],
    [0x01, 0x06, 0x14, 0x78],
    [0x01, 0x08, 0x40, 0x3a],
]

whirlpool_mat = [
	[0x01, 0x01, 0x03, 0x01, 0x05, 0x08, 0x09, 0x05],
	[0x05, 0x01, 0x01, 0x03, 0x01, 0x05, 0x08, 0x09],
	[0x09, 0x05, 0x01, 0x01, 0x03, 0x01, 0x05, 0x08],
	[0x08, 0x09, 0x05, 0x01, 0x01, 0x03, 0x01, 0x05],
	[0x05, 0x08, 0x09, 0x05, 0x01, 0x01, 0x03, 0x01],
	[0x01, 0x05, 0x08, 0x09, 0x05, 0x01, 0x01, 0x03],
	[0x03, 0x01, 0x05, 0x08, 0x09, 0x05, 0x01, 0x01],
	[0x01, 0x03, 0x01, 0x05, 0x08, 0x09, 0x05, 0x01]
]

whirlwind_m0 = [
    [0x5, 0x4, 0xa, 0x6, 0x2, 0xd, 0x8, 0x3],
    [0x4, 0x5, 0x6, 0xa, 0xd, 0x2, 0x3, 0x8],
    [0xa, 0x6, 0x5, 0x4, 0x8, 0x3, 0x2, 0xd],
    [0x6, 0xa, 0x4, 0x5, 0x3, 0x8, 0xd, 0x2],
    [0x2, 0xd, 0x8, 0x3, 0x5, 0x4, 0xa, 0x6],
    [0xd, 0x2, 0x3, 0x8, 0x4, 0x5, 0x6, 0xa],
    [0x8, 0x3, 0x2, 0xd, 0xa, 0x6, 0x5, 0x4],
    [0x3, 0x8, 0xd, 0x2, 0x6, 0xa, 0x4, 0x5]
]

def dyadic(vals):
    n = len(vals)

    mat = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            mat[i][j] = vals[i^j]

    return mat


whirlwind_m1 = dyadic([0x5, 0xe, 0x4, 0x7, 0x1, 0x3, 0xf, 0x8])

curupira = [
    [3, 2, 2],
    [4, 5, 4],
    [6, 6, 7]
]

grostl = [
    [0x02,0x02,0x03,0x04,0x05,0x03,0x05,0x07],
    [0x07,0x02,0x02,0x03,0x04,0x05,0x03,0x05],
    [0x05,0x07,0x02,0x02,0x03,0x04,0x05,0x03],
    [0x03,0x05,0x07,0x02,0x02,0x03,0x04,0x05],
    [0x05,0x03,0x05,0x07,0x02,0x02,0x03,0x04],
    [0x04,0x05,0x03,0x05,0x07,0x02,0x02,0x03],
    [0x03,0x04,0x05,0x03,0x05,0x07,0x02,0x02],
    [0x02,0x03,0x04,0x05,0x03,0x05,0x07,0x02]
]

rijndael_mat = [
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03, 0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02]
]

# hierocrypt 3

mds = [
  [0xc4, 0x65, 0xc8, 0x8b],
  [0x8b, 0xc4, 0x65, 0xc8],
  [0xc8, 0x8b, 0xc4, 0x65],
  [0x65, 0xc8, 0x8b, 0xc4]
]

mdsh = [
  [0x5, 0x5, 0xa, 0xe],
  [0xe, 0x5, 0x5, 0xa],
  [0xa, 0xe, 0x5, 0x5],
  [0x5, 0xa, 0xe, 0x5]
]

# hierocrypt l1

l1_mdsh = [
  [0x5, 0x7],
  [0xa, 0xb]
]

def poly_xtime_cost(poly):
	if poly == 0:
		return 0
	degree_mask = DEGREE_LIMIT_MASK
	degree = ORDER
	while (poly & degree_mask) == 0:
		degree_mask = degree_mask >> 1
		degree -= 1
	return degree

def poly_xor_cost(poly):
    mask = 1
    set_bits = 0
    current_bit = 0
    while current_bit < ORDER:
        if (poly & mask) != 0:
            set_bits += 1
        mask = mask << 1
        current_bit += 1
    return set_bits - 1

def matrix_xtime_cost(mat, dim):
    total_cost = 0
    for row in range(dim):
        row_cost = 0
        for col in range(dim):
            row_cost += poly_xtime_cost(mat[row][col])
        total_cost += row_cost
    return total_cost

def matrix_xor_cost(mat, dim):
    total_cost = 0
    for row in range(dim):
        row_cost = dim - 1
        for col in range(dim):
            row_cost += poly_xor_cost(mat[row][col])
        total_cost += row_cost
    return total_cost

def int_to_gf(int_poly):
    coeffs = []
    for x in bin(int_poly)[2:]:
        coeffs.append(int(x))

    return galois.Poly(coeffs, field=GF2)

def int_to_gf_mat(int_mat, field):
    rows = len(int_mat)
    cols = len(int_mat[0])

    gf_mat = field.Zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            gf_mat[i][j] = int_mat[i][j]

    return gf_mat

def print_mat_hex(m):
    for i in range(len(m)):
        row = []
        for j in range(len(m)):
            row.append(hex(m[i][j]))
        print(row)

def inverse_test(which_mat, which_field, label):
    shark_original = int_to_gf_mat(which_mat, which_field)
    shark_inv = np.linalg.inv(shark_original)

    print(label, "original")
    print(shark_original)
    print(label, "inversa")
    print(shark_inv)
    print_mat_hex(shark_inv)
    print("Multiplicando as duas")
    print(np.matmul(shark_original, shark_inv))

def tests():
    #inverse_test(shark_mat, shark_field, "shark")
    #inverse_test(square_mat, shark_field, "square")
    #inverse_test(bksq_mat, shark_field, "bksq")

    #inverse_test(rijndael_mat, rijndael_field, "rijndael")

    #inverse_test(anubis_mat, anubis_field, "anubis")
    #inverse_test(khazad_mat, anubis_field, "khazad")
    #inverse_test(tavares_mat, anubis_field, "tavares")
    #inverse_test(mds, hierocrypt_field, "hierocrypt gf256")

    print(hierocrypt_higher_field.properties)
    inverse_test(mdsh, hierocrypt_higher_field, "hierocrypt gf16")

def irreducible_poly_investigation():
    original_matrix = int_to_gf_mat(bksq_mat, shark_field)
    original_inverse = np.linalg.inv(original_matrix)

    print("Matriz original")
    print(original_matrix)
    print("Inversa (original)")
    print(original_inverse)
    print("Polinômio irredutível do corpo original:")
    print(shark_field.irreducible_poly)
    print("--------------------------")

    different_fields = [anubis_field, rijndael_field, hierocrypt_field]

    for field in different_fields:
        original_diff_field = int_to_gf_mat(bksq_mat, field)
        inverse_diff_field = np.linalg.inv(original_diff_field)
        print("Novo polinômio irredutível:")
        print(field.irreducible_poly)

        print("Inversa obtida com o novo polinômio")
        print(inverse_diff_field)
        print("Vendo se multiplicando dá a identidade, pra ter certeza que é inversa mesmo")
        print(np.matmul(original_diff_field, inverse_diff_field))
        print("Ok, tá certo!")

def hierocrypt_high():
    print("Matriz do Hierocrypt 3")
    matrix = int_to_gf_mat(mdsh, hierocrypt_higher_field)
    print(matrix)
    inv = np.linalg.inv(matrix)
    print("Inversa encontrada no código de referência:")
    print(inv)
    print("Em hexadecimal:")
    print_mat_hex(inv)

    polys = galois.irreducible_polys(2, 4)

    for p in polys:
        field = galois.GF(2**4, irreducible_poly = p)
        mat_new_field = int_to_gf_mat(mdsh, field)
        print("Inversa usando polinômio irredutível", p)
        inverse = np.linalg.inv(mat_new_field)
        print(inverse)

def hierocrypt_l1_high():
    print("Matriz do Hierocrypt L1")
    matrix = int_to_gf_mat(l1_mdsh, hierocrypt_higher_field)
    print(matrix)
    inv = np.linalg.inv(matrix)
    print("Inversa encontrada no código de referência:")
    print(inv)
    print("Em hexadecimal:")
    print_mat_hex(inv)

    polys = galois.irreducible_polys(2, 4)

    for p in polys:
        field = galois.GF(2**4, irreducible_poly = p)
        mat_new_field = int_to_gf_mat(l1_mdsh, field)
        print("Inversa usando polinômio irredutível", p)
        inverse = np.linalg.inv(mat_new_field)
        print(inverse)

def rijndael():
    original = int_to_gf_mat(rijndael_mat, rijndael_field)
    inv = np.linalg.inv(original)

    print("Rijndael - matrizes com o pol. irredutível especificado")
    print(original)
    print(inv)

    polys = galois.irreducible_polys(2, 8)

    print("Inversas com pols irredutíveis diferentes")

    for p in polys:
        field = galois.GF(2**8, irreducible_poly = p)
        mat_new_field = int_to_gf_mat(rijndael_mat, field)
        print("Inversa usando polinômio irredutível", p)
        inverse = np.linalg.inv(mat_new_field)
        print(inverse)

def square():
    original = int_to_gf_mat(square_mat, shark_field)
    inv = np.linalg.inv(original)

    print("Square - matrizes com o pol. irredutível especificado")
    print(original)
    print(inv)

    polys = galois.irreducible_polys(2, 8)

    print("Inversas com pols irredutíveis diferentes")

    for p in polys:
        field = galois.GF(2**8, irreducible_poly = p)
        mat_new_field = int_to_gf_mat(square_mat, field)
        print("Inversa usando polinômio irredutível", p)
        inverse = np.linalg.inv(mat_new_field)
        print(inverse)

def shark():
    original = int_to_gf_mat(shark_mat, shark_field)
    inv = np.linalg.inv(original)

    print("Shark - matrizes com o pol. irredutível especificado")
    print(original)
    print(inv)

    polys = galois.irreducible_polys(2, 8)

    print("Inversas com pols irredutíveis diferentes")

    for p in polys:
        field = galois.GF(2**8, irreducible_poly = p)
        mat_new_field = int_to_gf_mat(shark_mat, field)
        print("Inversa usando polinômio irredutível", p)
        inverse = np.linalg.inv(mat_new_field)
        print(inverse)

def khazad():
    original = int_to_gf_mat(khazad_mat, anubis_field)
    inv = np.linalg.inv(original)

    print("Khazad - matrizes com o pol. irredutível especificado")
    print(original)
    print(inv)

    polys = galois.irreducible_polys(2, 8)

    print("Inversas com pols irredutíveis diferentes")

    for p in polys:
        field = galois.GF(2**8, irreducible_poly = p)
        mat_new_field = int_to_gf_mat(khazad_mat, field)
        print("Inversa usando polinômio irredutível", p)
        inverse = np.linalg.inv(mat_new_field)
        print(inverse)

def anubis():
    original = int_to_gf_mat(anubis_mat, anubis_field)
    inv = np.linalg.inv(original)

    print("Khazad - matrizes com o pol. irredutível especificado")
    print(original)
    print(inv)

    polys = galois.irreducible_polys(2, 8)

    print("Inversas com pols irredutíveis diferentes")

    for p in polys:
        field = galois.GF(2**8, irreducible_poly = p)
        mat_new_field = int_to_gf_mat(anubis_mat, field)
        print("Inversa usando polinômio irredutível", p)
        inverse = np.linalg.inv(mat_new_field)
        print(inverse)

def anubis_vandermonde():
    hex2 = int_to_gf(0x02)
    hex6 = int_to_gf(0x06)
    hex8 = int_to_gf(0x08)

    hex2_2 = galois.pow(hex2, 2, tavares_khazad_anubis_poly)
    hex2_3 = galois.pow(hex2, 3, tavares_khazad_anubis_poly)

    print(hex2, hex(hex2.integer))
    print(hex2_2, hex(hex2_2.integer))
    print(hex2_3, hex(hex2_3.integer))

    hex6_2 = galois.pow(hex6, 2, tavares_khazad_anubis_poly)
    hex6_3 = galois.pow(hex6, 3, tavares_khazad_anubis_poly)

    print(hex6, hex(hex6.integer))
    print(hex6_2, hex(hex6_2.integer))
    print(hex6_3, hex(hex6_3.integer))

    hex8_2 = galois.pow(hex8, 2, tavares_khazad_anubis_poly)
    hex8_3 = galois.pow(hex8, 3, tavares_khazad_anubis_poly)

    print(hex8, hex(hex8.integer))
    print(hex8_2, hex(hex8_2.integer))
    print(hex8_3, hex(hex8_3.integer))

def anubis_vandermonde_invol():
    m = int_to_gf_mat(anubis_ke_mat, anubis_field)
    inv = np.linalg.inv(m)

    print_mat_hex(m)
    print("inv")
    print_mat_hex(inv)

    print("xor", matrix_xor_cost(anubis_ke_mat, 4))
    print("xtime", matrix_xtime_cost(anubis_ke_mat, 4))
    print("xor inv", matrix_xor_cost(inv, 4))
    print("xtime inv", matrix_xtime_cost(inv, 4))

def curupira_test():
    m = int_to_gf_mat(curupira, curupira_field)
    inv = np.linalg.inv(m)
    print(m)
    print(inv)

    print("xor", matrix_xor_cost(curupira, 3))
    print("xtime", matrix_xtime_cost(curupira, 3))

def get_curupira_ke():
	c = galois.Poly([0, 0, 0, 0, 1, 1, 1, 0, 0], field=GF2)
	c1 = galois.Poly([0, 0, 0, 0, 0, 0, 0, 1], field=GF2)+c
	intmat = [
        [c1.integer, c.integer, c.integer],
        [c.integer, c1.integer, c.integer],
        [c.integer, c.integer, c1.integer]
    ]
	return intmat

def curupira_ke_test():
    c = galois.Poly([0, 0, 0, 0, 1, 1, 1, 0, 0], field=GF2)
    print(c)
    c1 = galois.Poly([0, 0, 0, 0, 0, 0, 0, 1], field=GF2)+c
    print(c1)

    intmat = [
        [c1.integer, c.integer, c.integer],
        [c.integer, c1.integer, c.integer],
        [c.integer, c.integer, c1.integer]
    ]

    m = int_to_gf_mat(intmat, curupira_field)
    inv = np.linalg.inv(m)

    with curupira_field.display("poly"):
        print(m)
        print(inv)

    print("Original")
    print_mat_hex(m)
    print("Inv")
    print_mat_hex(inv)

    print("xor", matrix_xor_cost(intmat, 3))
    print("xtime", matrix_xtime_cost(intmat, 3))
    print("xor inv", matrix_xor_cost(inv, 3))
    print("xtime inv", matrix_xtime_cost(inv, 3))


def grostl_info():
    m = int_to_gf_mat(grostl, grostl_field)
    inv = np.linalg.inv(m)
    print_mat_hex(m)
    print("inv")
    print_mat_hex(inv)
    print("xor", matrix_xor_cost(grostl, 8))
    print("xtime", matrix_xtime_cost(grostl, 8))
    print("xor inv", matrix_xor_cost(inv, 8))
    print("xtime inv", matrix_xtime_cost(inv, 8))

def whirlpool_info():
	m = int_to_gf_mat(whirlpool_mat, whirlpool_field)
	print(m)
	print("xor", matrix_xor_cost(m, 8))
	print("xtime", matrix_xtime_cost(m, 8))

	inv = np.linalg.inv(m)
	print(inv)
	print("xor", matrix_xor_cost(inv, 8))
	print("xtime", matrix_xtime_cost(inv, 8))

	is_mds(inv)

def whirlwind_info():
	pass
	#m1 = int_to_gf_mat(whirlwind_m1, hierocrypt_higher_field)
	#m0 = int_to_gf_mat(whirlwind_m0, hierocrypt_higher_field)
    #print("m1")
    #print_mat_hex(m1)
    #print("m0")
    #print_mat_hex(m0)
    #print("ver se dyadic ta certa")
    #print_mat_hex(dyadic([0x5, 0x4, 0xa, 0x6, 0x2, 0xd, 0x8, 0x3]))
    #assert(whirlwind_m0 == dyadic([0x5, 0x4, 0xa, 0x6, 0x2, 0xd, 0x8, 0x3]))

    #print("xor m0", matrix_xor_cost(m0, 8))
    #print("xtime m0", matrix_xtime_cost(m0, 8))

    #print("xor m1", matrix_xor_cost(m1, 8))
    #print("xtime m1", matrix_xtime_cost(m1, 8))

def whirlwind_info_2():
	m1 = int_to_gf_mat(whirlwind_m1, hierocrypt_higher_field)
	m0 = int_to_gf_mat(whirlwind_m0, hierocrypt_higher_field)
	print("m1")
	print_mat_hex(m1)
	print("xor m1", matrix_xor_cost(m1, 8))
	print("xtime m1", matrix_xtime_cost(m1, 8))
	print("m0")
	print_mat_hex(m0)
	print("xor m0", matrix_xor_cost(m0, 8))
	print("xtime m0", matrix_xtime_cost(m0, 8))
	invm1 = np.linalg.inv(m1)
	invm0 = np.linalg.inv(m0)
	print("inv m1")
	print_mat_hex(invm1)
	print("xor invm1", matrix_xor_cost(invm1, 8))
	print("xtime invm1", matrix_xtime_cost(invm1, 8))
	print("inv m0")
	print_mat_hex(invm0)
	print("xor invm0", matrix_xor_cost(invm0, 8))
	print("xtime invm0", matrix_xtime_cost(invm0, 8))

def whirlwind_m0_mds_checker():
	m0 = int_to_gf_mat(whirlwind_m0, hierocrypt_higher_field)
	submatrix_checker(m0, hierocrypt_higher_field)

def whirlwind_m1_mds_checker():
	m1 = int_to_gf_mat(whirlwind_m1, hierocrypt_higher_field)
	submatrix_checker(m1, hierocrypt_higher_field)

def get_mu4():
	z = galois.Poly.Degrees([7, 6, 5, 4, 3, 2, 0])
	one = galois.Poly.Degrees([0])
	x = galois.Poly.Degrees([1])
	mu4 = [
        [one.integer, one.integer, one.integer, x.integer],
        [one.integer, z.integer, x.integer, one.integer],
        [z.integer, x.integer, one.integer, one.integer],
        [x.integer, one.integer, z.integer, one.integer]
    ]
	return mu4

def get_mu8():
	z = galois.Poly.Degrees([7, 6, 5, 4, 3, 2, 0])
	a = galois.Poly.Degrees([1, 0]).integer
	b = galois.Poly.Degrees([7, 1]).integer
	c = galois.Poly.Degrees([1]).integer
	d = galois.Poly.Degrees([2]).integer
	e = galois.Poly.Degrees([7, 6, 5, 4, 3, 2]).integer
	f = galois.Poly.Degrees([6, 5, 4, 3, 2, 1]).integer
	one = galois.Poly.Degrees([0])
	x = galois.Poly.Degrees([1])
	mu8 = [
        [1, 1, 1, 1, 1, 1, 1, a],
        [1, a, b, c, d, e, f, 1],
        [a, b, c, d, e, f, 1, 1],
        [b, c, d, e, f, 1, a, 1],
        [c, d, e, f, 1, a, b, 1],
        [d, e, f, 1, a, b, c, 1],
        [e, f, 1, a, b, c, d, 1],
        [f, 1, a, b, c, d, e, 1]
    ]
	return mu8

def fox():
    z = galois.Poly.Degrees([7, 6, 5, 4, 3, 2, 0])
    a = galois.Poly.Degrees([1, 0]).integer
    b = galois.Poly.Degrees([7, 1]).integer
    c = galois.Poly.Degrees([1]).integer
    d = galois.Poly.Degrees([2]).integer
    e = galois.Poly.Degrees([7, 6, 5, 4, 3, 2]).integer
    f = galois.Poly.Degrees([6, 5, 4, 3, 2, 1]).integer
    one = galois.Poly.Degrees([0])
    x = galois.Poly.Degrees([1])

    print(hex(a), hex(b), hex(c), hex(d), hex(e), hex(f))

    mu4 = [
        [one.integer, one.integer, one.integer, x.integer],
        [one.integer, z.integer, x.integer, one.integer],
        [z.integer, x.integer, one.integer, one.integer],
        [x.integer, one.integer, z.integer, one.integer]
    ]

    print_mat_hex(mu4)
    print("xor mu4", matrix_xor_cost(mu4, 4))
    print("xtime mu4", matrix_xtime_cost(mu4, 4))

    mu8 = [
        [1, 1, 1, 1, 1, 1, 1, a],
        [1, a, b, c, d, e, f, 1],
        [a, b, c, d, e, f, 1, 1],
        [b, c, d, e, f, 1, a, 1],
        [c, d, e, f, 1, a, b, 1],
        [d, e, f, 1, a, b, c, 1],
        [e, f, 1, a, b, c, d, 1],
        [f, 1, a, b, c, d, e, 1]
    ]

    print_mat_hex(mu8)
    print("xor mu8", matrix_xor_cost(mu8, 8))
    print("xtime mu8", matrix_xtime_cost(mu8, 8))

    mu4_gf = int_to_gf_mat(mu4, fox_field)
    mu4_inv = np.linalg.inv(mu4_gf)

    mu8_gf = int_to_gf_mat(mu8, fox_field)
    mu8_inv = np.linalg.inv(mu8_gf)

    print("mu4 inverse")
    print_mat_hex(mu4_inv)
    print("xor mu4 inv", matrix_xor_cost(mu4_inv, 4))
    print("xtime mu4 inv", matrix_xtime_cost(mu4_inv, 4))

    print("mu8 inverse")
    print_mat_hex(mu8_inv)
    print("xor mu8 inv", matrix_xor_cost(mu8_inv, 8))
    print("xtime mu8 inv", matrix_xtime_cost(mu8_inv, 8))

def submatrix_checker(mat, field):
	total_submats = 0

	submats_per_dim = {}

	check = True
	smallest_submat = []
	smallest_submat_dim = 100
	smallest_rows = []
	smallest_cols = []
	if np.linalg.det(mat) == 0:
		return False

	dim = len(mat)

	dim_list = [i for i in range(dim)]

	z = 1
	while z < dim:
		possibilities = list(itertools.combinations(dim_list, z))

		for rows_to_be_removed in possibilities:
			for columns_to_be_removed in possibilities:
				submat = np.delete(mat, rows_to_be_removed, axis=0)
				submat = np.delete(submat, columns_to_be_removed, axis=1)
				if np.linalg.det(submat) == 0:

					total_submats += 1
					if len(submat) in submats_per_dim:
						submats_per_dim[len(submat)] += 1
					else:
						submats_per_dim[len(submat)] = 1

					if len(submat) < smallest_submat_dim:
						smallest_submat = submat
						smallest_submat_dim = len(submat)
						smallest_rows = rows_to_be_removed
						smallest_cols = columns_to_be_removed
					print(np.linalg.det(submat))
					print("Linhas removidas:", rows_to_be_removed)
					print("Colunas removidas:", columns_to_be_removed)
					#print("Submatriz com determinante zero")
					#print(submat)
					#print("Matriz original")
					#print(mat)
					check = False
					#return False
		z += 1
	print("Menor submatriz com determinante zero")
	with field.display("poly"):
		print(smallest_submat)
	with field.display("int"):
		print(smallest_submat)
	print("Obtida removendo linhas", smallest_rows, "e colunas", smallest_cols)
	print("Matriz original")
	print_mat_hex(mat)
	print("---")
	print_mat_hex(smallest_submat)
	print("Total de submatrizes singulares:", total_submats)
	print("Submatrizes singulares por dimensão:", submats_per_dim)
	return check

def is_mds(mat):
	if np.linalg.det(mat) == 0:
		return False

	dim = len(mat)

	dim_list = [i for i in range(dim)]

	z = 1
	while z < dim:
		possibilities = list(itertools.combinations(dim_list, z))

		for rows_to_be_removed in possibilities:
			for columns_to_be_removed in possibilities:
				submat = np.delete(mat, rows_to_be_removed, axis=0)
				submat = np.delete(submat, columns_to_be_removed, axis=1)
				if np.linalg.det(submat) == 0:
					return False
		z += 1
	return True

class MatData():
	def __init__(self):
		self.det = 0
		self.det_mul_inverse = 0
		self.xor = 0
		self.xtime = 0
		self.involutory = False
		self.mds = False
		self.inv_det = 0
		self.inv_xor = 0
		self.inv_xtime = 0
		self.inv_involutory = False
		self.inv_mds = False
		self.mat = []
		self.inv = []

	def short_dict(self):
		d = self.__dict__
		d.pop("mat")
		d.pop("inv")
		d["det"] = hex(int(d["det"]))
		d["det_mul_inverse"] = hex(int(d["det_mul_inverse"]))
		d["inv_det"] = hex(int(d["inv_det"]))
		return d

	def __str__(self):
		return "det: " + str(hex(int(self.det))) + " xor: " + str(self.xor) + " xtime: " + str(self.xtime) + " involutory: " + str(self.involutory) + " mds: " + str(self.mds) + "\n" + "inv_det: " + str(hex(int(self.inv_det))) + " inv_xor: " + str(self.inv_xor) + " inv_xtime: " + str(self.inv_xtime) + " inv_involutory: " + str(self.inv_involutory) + " inv_mds: " + str(self.inv_mds)

def get_matrix_information_in_field(m, irreducible_poly):
	mat_data = MatData()

	identity = np.identity(len(m))

	order = irreducible_poly.degree
	field = galois.GF(2**order, irreducible_poly=irreducible_poly)
	mat = int_to_gf_mat(m, field)

	mat_data.mat = mat
	mat_data.det = np.linalg.det(mat)
	mat_data.det_mul_inverse = np.reciprocal(mat_data.det)

	print(mat_data.det_mul_inverse * mat_data.det)

	mat_data.xor = matrix_xor_cost(mat, len(mat))
	mat_data.xtime = matrix_xtime_cost(mat, len(mat))

	involutory = False
	if np.array_equal(np.matmul(mat, mat), identity):
		involutory = True

	mat_data.involutory = involutory
	mat_data.mds = is_mds(mat)
	inv = np.linalg.inv(mat)
	mat_data.inv = inv
	mat_data.inv_det = np.linalg.det(inv)
	mat_data.inv_xor = matrix_xor_cost(inv, len(inv))
	mat_data.inv_xtime = matrix_xtime_cost(inv, len(inv))

	involutory = False
	if np.array_equal(np.matmul(inv, inv), identity):
		involutory = True

	mat_data.inv_involutory = involutory

	#print("checagem mds")
	mat_data.inv_mds = is_mds(inv)
	#print("checagem mds ok")
	#print(mat_data)
	print("Inversa calculada:")
	print_mat_hex(inv)
	return mat_data

data_map = {}

def explore_fields(m, name, order, original_poly):
	data_map[name] = {}
	print("==", name, "==", "\n")

	polys = galois.irreducible_polys(2, order)
	#print("Matriz:")
	#print_mat_hex(m)

	smallest_xtime = 1000000000000000000
	smallest_xor = 1000000000000000000
	poly_xor = 0
	poly_xtime = 0

	original_xor = 0
	original_xtime = 0

	ORDER = order

	if ORDER == 8:
		DEGREE_LIMIT_MASK = 0x100
	if ORDER == 4:
		DEGREE_LIMIT_MASK = 0b10000

	print("Configurações dos polinômios: ORDER", ORDER, "DEGREE_MASK", bin(DEGREE_LIMIT_MASK))

	for p in polys:
		print("POLINÔMIO IRREDUTÍVEL: ", p)
		info = get_matrix_information_in_field(m, p)
		print(info)
		print("")
		data_map[name][p.string] = info.short_dict()

		if p == original_poly:
			original_xor = info.inv_xor
			original_xtime = info.inv_xtime

		if info.inv_mds:
			if info.inv_xor < smallest_xor:
				poly_xor = p
				smallest_xor = info.inv_xor

			if info.inv_xtime < smallest_xtime:
				poly_xtime = p
				smallest_xtime = info.inv_xtime


	print(name, "Inv best xtime:", smallest_xtime, "with", poly_xtime)
	print(name, "Inv best xor:", smallest_xor, "with", poly_xor)
	print(name, "Inv xtime:", original_xtime, "with original poly =", original_poly)
	print(name, "Inv xor:", original_xor, "with original poly =", original_poly)
	print("")
	#pprint.pprint(data_map)

def test_det():
	example_mat = [[1, 2], [3, 4]]
	m = int_to_gf_mat(example_mat, shark_field)
	with shark_field.display("poly"):
		print(m)
		print(np.linalg.det(m), type(np.linalg.det(m)), type(m[0][0]), type(shark_field.irreducible_poly))
		print(str(np.linalg.det(m)))

def get_csvs(csv_name):
	header = ['label', 'poly', 'det', 'det_mul_inverse', 'xor', 'xtime', 'involutory', 'mds', 'inv_det', 'inv_xor', 'inv_xtime', 'inv_involutory', 'inv_mds']
	rows = [header]
	for alg in data_map:
		for poly in data_map[alg]:
			row = [alg, poly]
			for key in ['det', 'det_mul_inverse', 'xor', 'xtime', 'involutory', 'mds', 'inv_det', 'inv_xor', 'inv_xtime', 'inv_involutory', 'inv_mds']:
				row.append(data_map[alg][poly][key])
			rows.append(row)

	with open(csv_name, "w") as f:
		writer = csv.writer(f)
		writer.writerows(rows)

def mds_data():
	#test_det()
	explore_fields(shark_mat, "SHARK", 8, shark_square_bksq_poly)
	explore_fields(square_mat, "SQUARE", 8, shark_square_bksq_poly)
	explore_fields(bksq_mat, "BKSQ", 8, shark_square_bksq_poly)
	explore_fields(tavares_mat, "Tavares", 8, tavares_khazad_anubis_poly)
	explore_fields(khazad_mat, "KHAZAD", 8, tavares_khazad_anubis_poly)
	explore_fields(anubis_mat, "Anubis", 8, tavares_khazad_anubis_poly)
	explore_fields(anubis_ke_mat, "Anubis (key schedule)", 8, tavares_khazad_anubis_poly)
	explore_fields(whirlwind_m0, "Whirlwind m0", 4, whirlwind_poly)
	explore_fields(whirlwind_m1, "Whirlwind m1", 4, whirlwind_poly)
	explore_fields(grostl, "Grostl", 8, rijndael_poly)
	explore_fields(curupira, "Curupira", 8, curupira_poly)
	explore_fields(get_curupira_ke(), "Curupira (ke)", 8, curupira_poly)
	explore_fields(rijndael_mat, "Rijndael", 8, rijndael_poly)
	explore_fields(mds, "Hierocrypt 3 and L1 (low)", 8, hierocrypt_poly)
	explore_fields(mdsh, "Hierocrypt 3 (high)", 4, whirlwind_poly)
	explore_fields(l1_mdsh, "Hierocrypt L1 (high)", 4, whirlwind_poly)
	explore_fields(get_mu4(), "FOX mu4", 8, fox_poly)
	explore_fields(get_mu8(), "FOX mu8", 8, fox_poly)
	explore_fields(whirlpool_mat, "Whirlpool", 8, tavares_khazad_anubis_poly)
	get_csvs("mds_data_summary_3.csv")

def mds_data_2():
	explore_fields(shark_mat, "SHARK", 8, shark_square_bksq_poly)
	explore_fields(square_mat, "SQUARE", 8, shark_square_bksq_poly)
	explore_fields(bksq_mat, "BKSQ", 8, shark_square_bksq_poly)
	explore_fields(tavares_mat, "Tavares", 8, tavares_khazad_anubis_poly)
	explore_fields(khazad_mat, "KHAZAD", 8, tavares_khazad_anubis_poly)
	explore_fields(anubis_mat, "Anubis", 8, tavares_khazad_anubis_poly)
	explore_fields(anubis_ke_mat, "Anubis (key schedule)", 8, tavares_khazad_anubis_poly)
	explore_fields(whirlwind_m0, "Whirlwind m0", 4, whirlwind_poly)
	explore_fields(whirlwind_m1, "Whirlwind m1", 4, whirlwind_poly)
	explore_fields(grostl, "Grostl", 8, rijndael_poly)
	explore_fields(curupira, "Curupira", 8, curupira_poly)
	explore_fields(get_curupira_ke(), "Curupira (ke)", 8, curupira_poly)
	explore_fields(rijndael_mat, "Rijndael", 8, rijndael_poly)
	explore_fields(mds, "Hierocrypt 3 and L1 (low)", 8, hierocrypt_poly)
	explore_fields(mdsh, "Hierocrypt 3 (high)", 4, whirlwind_poly)
	explore_fields(l1_mdsh, "Hierocrypt L1 (high)", 4, whirlwind_poly)
	explore_fields(get_mu4(), "FOX mu4", 8, fox_poly)
	explore_fields(get_mu8(), "FOX mu8", 8, fox_poly)
	explore_fields(whirlpool_mat, "Whirlpool", 8, tavares_khazad_anubis_poly)
	get_csvs("mds_data_summary_4.csv")

def hiero_non_mds():
	print("8x8 xor", matrix_xor_cost(hiero_8x8, 8))
	print("8x8 xtime", matrix_xtime_cost(hiero_8x8, 8))
	print("16x16 xor", matrix_xor_cost(hiero_16x16, 16))
	print("16x16 xtime", matrix_xtime_cost(hiero_16x16, 16))

def rcirc(first_row):
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
	print(rows)

def shirai_costs():
	s0 = int_to_gf_mat(rcirc([1, 1, 2, 1, 5, 8, 9, 4]), whirlpool_field)
	s1 = int_to_gf_mat(rcirc([1, 1, 2, 1, 6, 9, 8, 3]), whirlpool_field)
	s2 = int_to_gf_mat(rcirc([1, 1, 2, 1, 8, 9, 4, 5]), whirlpool_field)
	s3 = int_to_gf_mat(rcirc([1, 1, 2, 1, 9, 6, 4, 3]), whirlpool_field)
	s4 = int_to_gf_mat(rcirc([1, 1, 2, 6, 5, 9, 1, 8]), whirlpool_field)
	s5 = int_to_gf_mat(rcirc([1, 1, 3, 1, 4, 9, 5, 6]), whirlpool_field)
	s6 = int_to_gf_mat(rcirc([1, 1, 3, 1, 8, 4, 9, 6]), whirlpool_field)
	s7 = int_to_gf_mat(rcirc([1, 1, 4, 1, 8, 5, 2, 9]), whirlpool_field)
	s8 = int_to_gf_mat(rcirc([1, 1, 4, 1, 9, 3, 2, 6]), whirlpool_field)
	s9 = int_to_gf_mat(rcirc([1, 1, 4, 3, 6, 8, 1, 9]), whirlpool_field)
	s10 = int_to_gf_mat(rcirc([1, 1, 5, 1, 4, 6, 3, 9]), whirlpool_field)
	s11 = int_to_gf_mat(rcirc([1, 1, 5, 8, 2, 9, 1, 6]), whirlpool_field)
	s12 = int_to_gf_mat(rcirc([1, 1, 8, 1, 6, 3, 2, 9]), whirlpool_field)
	s13 = int_to_gf_mat(rcirc([1, 1, 8, 2, 4, 5, 1, 9]), whirlpool_field)

	#shirai = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13]
	shirai = [s8]
	for s in shirai:
		print("xor", matrix_xor_cost(s, 8))

	for s in shirai:
		print("xtime", matrix_xtime_cost(s, 8))

	for s in shirai:
		inv = np.linalg.inv(s)
		print("ixr", matrix_xor_cost(inv, 8), "ixt", matrix_xtime_cost(inv, 8))
		print_mat_hex(inv)
		print("---")

def hamming_weight(vector):
	hw = 0
	for element in vector:
		if element %2 != 0:
			hw += 1
	return hw

def hierocrypt_8x8_branch_number():
	mat = [[1,0,1,0,1,1,1,0],
	[1,1,0,1,1,1,1,1],
	[1,1,1,0,0,1,1,1],
	[0,1,0,1,1,1,0,1],
	[1,1,0,1,0,1,0,1],
	[1,1,1,0,1,0,1,0],
	[1,1,1,1,1,1,0,1],
	[1,0,1,0,1,0,1,1]]
	a = [1, 1, 0, 0, 0, 0, 0, 0]
	theta = np.dot(mat, np.array([a]).T)
	wa = hamming_weight(a)
	wtheta = hamming_weight(theta)
	branch = wa + wtheta
	print(theta)
	print("wa = ", wa, "wtheta = ", wtheta, "branch =", branch)

def hierocrypt_16x16_branch_number():
	# matrix
	mat = [[1,0,1,0,1,0,1,0,1,1,0,1,1,1,1,1],
		   [1,1,0,1,1,1,0,1,1,1,1,0,0,1,1,1],
		   [1,1,1,0,1,1,1,0,1,1,1,1,0,0,1,1],
		   [0,1,0,1,0,1,0,1,1,0,1,0,1,1,1,0],
		   [1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,1],
		   [0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0],
		   [0,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1],
		   [1,1,1,0,0,1,0,1,0,1,0,1,1,0,1,0],
		   [1,1,0,1,1,1,1,1,1,0,1,0,1,0,1,0],
		   [1,1,1,0,0,1,1,1,1,1,0,1,1,1,0,1],
		   [1,1,1,1,0,0,1,1,1,1,1,0,1,1,1,0],
		   [1,0,1,0,1,1,1,0,0,1,0,1,0,1,0,1],
		   [1,0,1,0,1,1,0,1,1,1,1,1,1,0,1,0],
		   [1,1,0,1,1,1,1,0,0,1,1,1,1,1,0,1],
		   [1,1,1,0,1,1,1,1,0,0,1,1,1,1,1,0],
		   [0,1,0,1,1,0,1,0,1,1,1,0,0,1,0,1]]

	v1  = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	v2  = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	v3  = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
	v4  = [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
	v5  = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
	v6  = [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
	v7  = [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
	v8  = [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
	v9  = [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
	v10 = [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
	v11 = [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
	v12 = [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
	v13 = [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
	v14 = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
	v15 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
	v16 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]

	vecs = [v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16]

	min_branch = 20
	min_a = []
	min_wtheta = []
	min_theta = []

	for v in vecs:
		mult = np.dot(mat, np.array([v]).T)
		wa = hamming_weight(v)
		wtheta = hamming_weight(mult)
		#print("a =", v, "w(a) =", wa)
		#print("theta(a) =", mult, "w(theta(a)) =", wtheta)
		branch = wa + wtheta
		#print("branch =", branch)

		if branch < min_branch:
			min_branch = branch
			min_a = v
			min_wtheta = wtheta
			min_theta = mult

	print(min_branch, "obtido com a =", min_a, "e w(theta) = ", min_wtheta, "(theta = ", min_theta ,")")

def led_info():
	mat = [
		[4, 1, 2, 2],
		[8, 6, 5, 6],
		[0x0b, 0x0e, 0x0a, 9],
		[2, 2, 0x0f, 0x0b]
	]
	led_mat = int_to_gf_mat(mat, led_field)
	# is mds?
	print(is_mds(led_mat))
	# xor
	print("xor", matrix_xor_cost(led_mat, 4))
	# xtime
	print("xtime", matrix_xtime_cost(led_mat, 4))

	# inverse
	inv = np.linalg.inv(led_mat)
	print("inverse")
	print_mat_hex(inv)
	# inv xor
	print("xor", matrix_xor_cost(inv, 4))
	# inv xtime
	print("xtime", matrix_xtime_cost(inv, 4))
	print(is_mds(inv))

def get_mat_info_for_mds_table(mat, field, dim, name):
	print(name)
	alg_mat = int_to_gf_mat(mat, field)
	print_mat_hex(alg_mat)
	print("mds", is_mds(alg_mat))
	print("xor", matrix_xor_cost(alg_mat, dim))
	print("xtime", matrix_xtime_cost(alg_mat, dim))

	inv = np.linalg.inv(alg_mat)
	print("inverse")
	print_mat_hex(inv)
	print("xor", matrix_xor_cost(inv, dim))
	print("xtime", matrix_xtime_cost(inv, dim))
	print("mds", is_mds(inv))

photon4_a100 = [
	[1, 2, 9, 9, 2],
	[2, 5, 3, 8, 13],
	[13, 11, 10, 12, 1],
	[1, 15, 2, 3, 14],
	[14, 14, 8, 5, 12]
]

photon4_a144 = [
	[1, 2, 8, 5, 8, 2],
	[2, 5, 1, 2, 6, 12],
	[12, 9, 15, 8, 8, 13],
	[13, 5, 11, 3, 10, 1],
	[1, 15, 13, 14, 11, 8],
	[8, 2, 3, 3, 2, 8]
]

photon4_a196 = [
	[1, 4, 6, 1, 1, 6, 4],
	[4, 2, 15, 2, 5, 10, 5],
	[5, 3, 15, 10, 7, 8, 13],
	[13, 4, 11, 2, 7, 15, 9],
	[9, 15, 7, 2, 11, 4, 13],
	[13, 8, 7, 10, 15, 3, 5],
	[5, 10, 5, 2, 15, 2, 4]
]

photon4_a256 = [
	[2, 4, 2, 11, 2, 8, 5, 6],
	[12, 9, 8, 13, 7, 7, 5, 2],
	[4, 4, 13, 13, 9, 4, 13, 9],
	[1, 6, 5, 1, 12, 13, 15, 14],
	[15, 12, 9, 13, 14, 5, 14, 13],
	[9, 14, 5, 15, 4, 12, 9, 6],
	[12, 2, 2, 10, 3, 1, 1, 14],
	[15, 1, 13, 10, 5, 10, 2, 3]
]

photon8_a288 = [
	[2, 3, 1, 2, 1, 4],
	[8, 14, 7, 9, 6, 17],
	[34, 59, 31, 37, 24, 66],
	[132, 228, 121, 155, 103, 11],
	[22, 153, 239, 111, 144, 75],
	[150, 203, 210, 121, 36, 167]
]

elcio = [[0x01, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x10, 0x02, 0x1e],
[0x03, 0x01, 0x05, 0x04, 0x07, 0x06, 0x09, 0x08, 0x0b, 0x0a, 0x0d, 0x0c, 0x10, 0x0e, 0x1e, 0x02],
[0x04, 0x05, 0x01, 0x03, 0x08, 0x09, 0x06, 0x07, 0x0c, 0x0d, 0x0a, 0x0b, 0x02, 0x1e, 0x0e, 0x10],
[0x05, 0x04, 0x03, 0x01, 0x09, 0x08, 0x07, 0x06, 0x0d, 0x0c, 0x0b, 0x0a, 0x1e, 0x02, 0x10, 0x0e],
[0x06, 0x07, 0x08, 0x09, 0x01, 0x03, 0x04, 0x05, 0x0e, 0x10, 0x02, 0x1e, 0x0a, 0x0b, 0x0c, 0x0d],
[0x07, 0x06, 0x09, 0x08, 0x03, 0x01, 0x05, 0x04, 0x10, 0x0e, 0x1e, 0x02, 0x0b, 0x0a, 0x0d, 0x0c],
[0x08, 0x09, 0x06, 0x07, 0x04, 0x05, 0x01, 0x03, 0x02, 0x1e, 0x0e, 0x10, 0x0c, 0x0d, 0x0a, 0x0b],
[0x09, 0x08, 0x07, 0x06, 0x05, 0x04, 0x03, 0x01, 0x1e, 0x02, 0x10, 0x0e, 0x0d, 0x0c, 0x0b, 0x0a],
[0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x10, 0x02, 0x1e, 0x01, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09],
[0x0b, 0x0a, 0x0d, 0x0c, 0x10, 0x0e, 0x1e, 0x02, 0x03, 0x01, 0x05, 0x04, 0x07, 0x06, 0x09, 0x08],
[0x0c, 0x0d, 0x0a, 0x0b, 0x02, 0x1e, 0x0e, 0x10, 0x04, 0x05, 0x01, 0x03, 0x08, 0x09, 0x06, 0x07],
[0x0d, 0x0c, 0x0b, 0x0a, 0x1e, 0x02, 0x10, 0x0e, 0x05, 0x04, 0x03, 0x01, 0x09, 0x08, 0x07, 0x06],
[0x0e, 0x10, 0x02, 0x1e, 0x0a, 0x0b, 0x0c, 0x0d, 0x06, 0x07, 0x08, 0x09, 0x01, 0x03, 0x04, 0x05],
[0x10, 0x0e, 0x1e, 0x02, 0x0b, 0x0a, 0x0d, 0x0c, 0x07, 0x06, 0x09, 0x08, 0x03, 0x01, 0x05, 0x04],
[0x02, 0x1e, 0x0e, 0x10, 0x0c, 0x0d, 0x0a, 0x0b, 0x08, 0x09, 0x06, 0x07, 0x04, 0x05, 0x01, 0x03],
[0x1e, 0x02, 0x10, 0x0e, 0x0d, 0x0c, 0x0b, 0x0a, 0x09, 0x08, 0x07, 0x06, 0x05, 0x04, 0x03, 0x01]]

def look_for_small_singular_submat(mat, small_dim, field):
	total_submats = 0

	check = True
	smallest_submat = []
	smallest_submat_dim = 100
	smallest_rows = []
	smallest_cols = []
	if np.linalg.det(mat) == 0:
		return False

	dim = len(mat)

	dim_list = [i for i in range(dim)]

	z = dim - small_dim
	print(z)
	possibilities = list(itertools.combinations(dim_list, z))

	for rows_to_be_removed in possibilities:
		for columns_to_be_removed in possibilities:
			submat = np.delete(mat, rows_to_be_removed, axis=0)
			submat = np.delete(submat, columns_to_be_removed, axis=1)
			if np.linalg.det(submat) == 0:

				total_submats += 1

				#print(np.linalg.det(submat))
				print("Linhas removidas:", rows_to_be_removed)
				print("Colunas removidas:", columns_to_be_removed)
				print("Hexadecimal singular submatrix:")
				print_mat_hex(submat)
				print("Polynomial singular submatrix:")
				with field.display("poly"):
					print(submat)
				check = False

	print("Total de submatrizes singulares:", total_submats)
	return check

photon4x4_mat = [
	[1, 2, 1, 4],
	[4, 9, 6, 17],
	[17, 38, 24, 66],
	[66, 149, 100, 11]
]

joltik = [
	[1, 4, 9, 13],
	[4, 1, 13, 9],
	[9, 13, 1, 4],
	[13, 9, 4, 1]
]

get_mat_info_for_mds_table(joltik, photon4cells_field, 4, "joltik")
