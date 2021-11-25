from field_args import *

discrete_log_inverse = [0 for i in range(TWO_ORDER_POWER)]
discrete_log = [0 for i in range(TWO_ORDER_POWER)]
initialized_logs = False

def init_discrete_log(): 
    global initialized_logs
      
    if initialized_logs == True:
        return
    
    discrete_log_inverse[0] = 1
    for i in range(1, TWO_ORDER_POWER):
        j = discrete_log_inverse[i-1] << 1
        if j & DEGREE_LIMIT_MASK:
            j = j ^ IRREDUCIBLE_POLY
        discrete_log_inverse[i] = j
    
    discrete_log[0] = 0
    for i in range(1, TWO_ORDER_POWER-1):
        discrete_log[discrete_log_inverse[i]] = i
    
    initialized_logs = True

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
        print("Row", row, "costs", row_cost, "xtime")
        total_cost += row_cost
    print("The full matrix costs", total_cost, "xtime")
    return total_cost

def matrix_xor_cost(mat, dim):
    total_cost = 0
    for row in range(dim):
        row_cost = dim - 1
        for col in range(dim):
            row_cost += poly_xor_cost(mat[row][col])
        print("Row", row, "costs", row_cost, "xor")
        total_cost += row_cost
    print("The full matrix costs", total_cost, "xor")
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
    
    init_discrete_log()
    modulus = TWO_ORDER_POWER-1
    return discrete_log_inverse[(discrete_log[poly1] + discrete_log[poly2]) % modulus];

def invert_poly(poly):
    if poly == 0:
        print("0 is not invertible!")
        return -1
    
    init_discrete_log()
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