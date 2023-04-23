from metrics_and_flags import *

def toep(sequence, n):
    seq_size = len(sequence)
    positive_indexes = [i for i in range(n)]
    negative_indexes = [-i for i in range(1,n)]

    seq_dict = {}
    for i in positive_indexes:
        seq_dict[i] = sequence[i]
    
    actual_vector_index = n
    for i in negative_indexes:
        seq_dict[i] = sequence[actual_vector_index]
        actual_vector_index += 1
    
    lower = 0
    upper = n-1

    matrix = []
    row = 1
    while row <= n:
        row_values = [seq_dict[i] for i in range(lower,upper+1)]
        lower -= 1
        upper -= 1
        row += 1
        matrix.append(row_values)
    
    return matrix

def poly_string_to_integer(poly_string_mat):
    rows = len(poly_string_mat)
    cols = len(poly_string_mat[0])

    output_mat = [[0 for j in range(cols)] for i in range(rows)]

    for i in range(rows):
        for j in range(cols):
            poly_string = poly_string_mat[i][j]
            poly = galois.Poly.Str(poly_string, field=GF2)
            integer = poly._integer
            #print(poly, "->", bin(integer), "->", integer)
            output_mat[i][j] = integer
    
    return output_mat

power_table = {
    "1": "1",
    "x": "x",
    "x^{253}": "x^7 + x^4 + 1",
    "x^{252}": "x^7 + x^5 + x^3 + 1",
    "x^{157}": "x + 1",
    "x^{158}": "x^2 + x",
    "x^{254}": "x^7 + x^6 + x^5 + 1",
    "x^2": "x^2",
}

sarkar2_powers = ["1", "1", "x", "x^{253}", "1", "x^{253}", "x^{252}", "x^{157}", "x^{158}", "x^{253}", "x^{254}", "x", "x^{254}", "x^2", "x"]
print(toep(sarkar2_powers, 8))
sarkar2_vals = [power_table[i] for i in sarkar2_powers]
#print(sarkar1_vals)
sarkar2_str = toep(sarkar2_vals, 8)
sarkar2 = poly_string_to_integer(sarkar2_str)
get_mat_info_for_mds_table(sarkar1, GF2_8, b.degree, "Sarkar 2")