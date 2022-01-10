#GF(2^8) #GF(2^4) (Hierocrypt)

ORDER = 8 #8 #4
TWO_ORDER_POWER = 256 #256 #16

SHARK_POLY =    0x1f5
KHAZAD_POLY =   0b100011101
TAVARES_POLY = 0b100011101
SQUARE_POLY =   0x1f5
BKSQ_POLY = 0b111110101
RIJNDAEL_POLY = 0x11b
HIEROCRYPT_POLY = 0x163

DEGREE_LIMIT_MASK = 0x100 #0x100 #0b10000
IRREDUCIBLE_POLY = SHARK_POLY

square_mat = [
		[0x02, 0x01, 0x01, 0x03],
		[0x03, 0x02, 0x01, 0x01],
		[0x01, 0x03, 0x02, 0x01],
		[0x01, 0x01, 0x03, 0x02]
	]
	
square_mat_inv = [
		[0x0e, 0x09, 0x0d, 0x0b],
		[0x0b, 0x0e, 0x09, 0x0d],
		[0x0d, 0x0b, 0x0e, 0x09],
		[0x09, 0x0d, 0x0b, 0x0e]
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
	
shark_mat_inv = [
		[0xe7, 0x30, 0x90, 0x85, 0xd0, 0x4b, 0x91, 0x41],
		[0x53, 0x95, 0x9b, 0xa5, 0x96, 0xbc, 0xa1, 0x68],
		[0x02, 0x45, 0xf7, 0x65, 0x5c, 0x1f, 0xb6, 0x52],
		[0xa2, 0xca, 0x22, 0x94, 0x44, 0x63, 0x2a, 0xa2],
		[0xfc, 0x67, 0x8e, 0x10, 0x29, 0x75, 0x85, 0x71],
		[0x24, 0x45, 0xa2, 0xcf, 0x2f, 0x22, 0xc1, 0x0e],
		[0xa1, 0xf1, 0x71, 0x40, 0x91, 0x27, 0x18, 0xa5],
		[0x56, 0xf4, 0xaf, 0x32, 0xd2, 0xa4, 0xdc, 0x71]
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

rijndael_mat = [
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03, 0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02]
]

rijndael_mat_inv = [
    [0x0e, 0x0b, 0x0d, 0x09],
    [0x09, 0x0e, 0x0b, 0x0d],
    [0x0d, 0x09, 0x0e, 0x0b],
    [0x0b, 0x0d, 0x09, 0x0e]
]

bksq_mat = [
    [3, 2, 2],
    [2, 3, 2],
    [2, 2, 3]
]

bksq_mat_inv = [
    [0xac, 0xad, 0xad],
    [0xad, 0xac, 0xad],
    [0xad, 0xad, 0xac]
]

# hierocrypt 3

mds = [
  [0xc4, 0x65, 0xc8, 0x8b],
  [0x8b, 0xc4, 0x65, 0xc8],
  [0xc8, 0x8b, 0xc4, 0x65],
  [0x65, 0xc8, 0x8b, 0xc4]
]

mds_inv = [
  [0x82, 0xc4, 0x34, 0xf6],
  [0xf6, 0x82, 0xc4, 0x34],
  [0x34, 0xf6, 0x82, 0xc4],
  [0xc4, 0x34, 0xf6, 0x82]
]

mdsh = [
  [0x5, 0x5, 0xa, 0xe],
  [0xe, 0x5, 0x5, 0xa],
  [0xa, 0xe, 0x5, 0x5],
  [0x5, 0xa, 0xe, 0x5]
]

mdsh_inv = [
  [0xb, 0xe, 0xe, 0x6],
  [0x6, 0xb, 0xe, 0xe],
  [0xe, 0x6, 0xb, 0xe],
  [0xe, 0xe, 0x6, 0xb]
]

# hierocrypt l1

l1_mdsh = [
  [0x5, 0x7],
  [0xa, 0xb]
]

l1_mdsh_inv = [
  [0xc, 0xa],
  [0x5, 0xb]
]

def init_discrete_log():
    discrete_log_inverse = [0 for i in range(TWO_ORDER_POWER)]
    discrete_log = [0 for i in range(TWO_ORDER_POWER)]
    
    discrete_log_inverse[0] = 1
    for i in range(1, TWO_ORDER_POWER):
        j = discrete_log_inverse[i-1] << 1
        if j & DEGREE_LIMIT_MASK:
            j = j ^ IRREDUCIBLE_POLY
        discrete_log_inverse[i] = j
    
    discrete_log[0] = 0
    for i in range(1, TWO_ORDER_POWER-1):
        discrete_log[discrete_log_inverse[i]] = i
    
    return discrete_log, discrete_log_inverse

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

def add_poly(poly1, poly2):
    return poly1 ^ poly2

def subtract_poly(poly1, poly2):
    return poly1 ^ poly2

def multiply_poly(poly1, poly2):
    if poly1 == 0:
        return 0
    if poly2 == 0:
        return 0
    
    discrete_log, discrete_log_inverse = init_discrete_log()
    modulus = TWO_ORDER_POWER-1
    return discrete_log_inverse[(discrete_log[poly1] + discrete_log[poly2]) % modulus];

def invert_poly(poly):
    if poly == 0:
        print("0 is not invertible!")
        return -1
    
    discrete_log, discrete_log_inverse = init_discrete_log()
    modulus = TWO_ORDER_POWER - 1
    return discrete_log_inverse[-discrete_log[poly] + modulus]

def matrix_multiplication(mat1, mat2, dim):
    result = []
    for i in range(dim):
        result.append([0])
        for j in range(dim):
            result[i].append(0)
    
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                mul = multiply_poly(mat1[i][k], mat2[k][j])
                add = add_poly(result[i][j], mul)
                result[i][j] = add
    
    return result

def get_determinant(mat, n):
    D = 0
    if n == 1:
        return mat[0][0]

    for f in range(n):
        temp = get_matrix_minor(mat, 0, f)
        recursive_det = get_determinant(temp, n-1)
        mul = multiply_poly(mat[0][f], recursive_det)
        D = add_poly(D, mul)
        
    return D

def get_matrix_minor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def transpose_matrix(m):
    dim = len(m)
    transpose = [[0 for i in range(dim)] for j in range(dim)]
    for i in range(dim):
        for j in range(dim):
            transpose[i][j] = m[j][i]
    return transpose

def invert_matrix(mat, dim):
    determinant = get_determinant(mat, dim)
    
    if determinant == 0:
        print("Matrix is not invertible!")
        return
    
    determinant_inverse = invert_poly(determinant)
    
    if dim == 2:
        a = multiply_poly(mat[1][1], determinant_inverse)
        b = multiply_poly(mat[0][1], determinant_inverse)
        c = multiply_poly(mat[1][0], determinant_inverse)
        d = multiply_poly(mat[0][0], determinant_inverse)
            
        return [[a, b],[c, d]]
    
    cofactors = []
    for r in range(dim):
        cofactor_row = []
        for c in range(dim):
            minor = get_matrix_minor(mat, r, c)
            cofactor_row.append(get_determinant(minor, dim-1))
        cofactors.append(cofactor_row)
    
    cofactors = transpose_matrix(cofactors)
        
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = multiply_poly(cofactors[r][c], determinant_inverse)
    return cofactors

def print_mat_hex(m):
    for i in range(len(m)):
        row = []
        for j in range(len(m)):
            row.append(hex(m[i][j]))
        print(row)

def inv_test(mat, mat_inv, dim, label):
    print("poly: ", hex(IRREDUCIBLE_POLY))
    inv = invert_matrix(mat, dim)
    original = invert_matrix(inv, dim)
    
    print(label, "- matriz original")
    print_mat_hex(mat)
    print(label, "- invertendo a original")
    print_mat_hex(inv)
    print(label, "- matriz inversa pra comparar")
    print_mat_hex(mat_inv)
    print(label, "- invertendo a inversa pra obter a original")
    print_mat_hex(original)
    print(label, "Teste de multiplicação (deve dar identidade)")
    identity = matrix_multiplication(mat, mat_inv, dim)
    print_mat_hex(identity)

inv_test(shark_mat, shark_mat_inv, 8, "shark")
