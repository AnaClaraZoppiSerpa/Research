import galois
import numpy as np

DEGREE_LIMIT_MASK = 0x100
ORDER = 8

GF2 = galois.GF(2)

shark_square_bksq_poly = galois.Poly([1, 1, 1, 1, 1, 0, 1, 0, 1], field=GF2)
tavares_khazad_anubis_poly = galois.Poly([1, 0, 0, 0, 1, 1, 1, 0, 1], field=GF2)
rijndael_poly = galois.Poly([1, 0, 0, 0, 1, 1, 0, 1, 1], field=GF2)
hierocrypt_poly = galois.Poly([1, 0, 1, 1, 0, 0, 0, 1, 1], field=GF2)
curupira_poly = galois.Poly([1, 0, 1, 0, 0, 1, 1, 0, 1], field=GF2)
fox_poly = galois.Poly.Degrees([8,7,6,5,4,3,0])

shark_field = galois.GF(2**8, irreducible_poly=shark_square_bksq_poly)
anubis_field = galois.GF(2**8, irreducible_poly=tavares_khazad_anubis_poly)
rijndael_field = galois.GF(2**8, irreducible_poly=rijndael_poly)
hierocrypt_field = galois.GF(2**8, irreducible_poly=hierocrypt_poly)
hierocrypt_higher_field = galois.GF(2**4)
curupira_field = galois.GF(2**8, irreducible_poly=curupira_poly)
grostl_field = galois.GF(2**8, irreducible_poly=rijndael_poly) # Grostl uses the same poly!
fox_field = galois.GF(2**8, irreducible_poly=fox_poly)

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
    
    print(m)
    print(inv)
    
    print("xor", matrix_xor_cost(anubis_ke_mat, 4))
    print("xtime", matrix_xtime_cost(anubis_ke_mat, 4))
    
def curupira_test():
    m = int_to_gf_mat(curupira, curupira_field)
    inv = np.linalg.inv(m)
    print(m)
    print(inv)
    
    print("xor", matrix_xor_cost(curupira, 3))
    print("xtime", matrix_xtime_cost(curupira, 3))

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
    print(m)
    print(inv)
    
    print("xor", matrix_xor_cost(intmat, 3))
    print("xtime", matrix_xtime_cost(intmat, 3))
    

def grostl_info():
    m = int_to_gf_mat(grostl, grostl_field)
    inv = np.linalg.inv(m)
    print(m)
    print(inv)
    print("xor", matrix_xor_cost(grostl, 8))
    print("xtime", matrix_xtime_cost(grostl, 8))

def whirlwind_info():
    #print("m1")
    #print_mat_hex(whirlwind_m1)
    #print("m0")
    #print_mat_hex(whirlwind_m0)
    #print("ver se dyadic ta certa")
    #print_mat_hex(dyadic([0x5, 0x4, 0xa, 0x6, 0x2, 0xd, 0x8, 0x3]))
    #assert(whirlwind_m0 == dyadic([0x5, 0x4, 0xa, 0x6, 0x2, 0xd, 0x8, 0x3]))
    
    print("xor m0", matrix_xor_cost(whirlwind_m0, 8))
    print("xtime m0", matrix_xtime_cost(whirlwind_m0, 8))
    
    print("xor m1", matrix_xor_cost(whirlwind_m1, 8))
    print("xtime m1", matrix_xtime_cost(whirlwind_m1, 8))

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
    
fox()
































