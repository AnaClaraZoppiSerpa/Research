import galois
import numpy as np

GF2 = galois.GF(2)

shark_square_bksq_poly = galois.Poly([1, 1, 1, 1, 1, 0, 1, 0, 1], field=GF2)
tavares_khazad_anubis_poly = galois.Poly([1, 0, 0, 0, 1, 1, 1, 0, 1], field=GF2)
rijndael_poly = galois.Poly([1, 0, 0, 0, 1, 1, 0, 1, 1], field=GF2)
hierocrypt_poly = galois.Poly([1, 0, 1, 1, 0, 0, 0, 1, 1], field=GF2)

shark_field = galois.GF(2**8, irreducible_poly=shark_square_bksq_poly)
anubis_field = galois.GF(2**8, irreducible_poly=tavares_khazad_anubis_poly)
rijndael_field = galois.GF(2**8, irreducible_poly=rijndael_poly)
hierocrypt_field = galois.GF(2**8, irreducible_poly=hierocrypt_poly)
hierocrypt_higher_field = galois.GF(2**4)

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
    [],
    [],
    [],
    [],
]

fox_mu8 = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

fox_mu4 = [
    [],
    [],
    [],
    []
]

whirlwind_m0 = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

curupira = [
    [],
    [],
    []
]

grostl = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
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

anubis()
