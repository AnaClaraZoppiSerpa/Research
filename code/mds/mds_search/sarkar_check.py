from metrics_and_flags import *

# TODO: Check Toep and Hank because there might be a mistake in them!

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

#% GF(2^4)
#% x^4+x+1
#% 8x8

GF2 = galois.GF(2)
a = galois.Poly.Str("x^4 + x + 1", field=GF2)
GF2_4 = galois.GF(2**4, irreducible_poly=a)

#print(GF2_4.properties)
#print(GF2_4.primitive_element)

#\begin{equation}\label{mat:sarkar-1}
#Toep(x, 1, x^4, 1, x^5, x^{14}, x^7, x^8, x^3, x^6, x^{14}, x^{14}, x^8, x^6, x^3)
#\end{equation}

# https://math.stackexchange.com/questions/4104767/is-x-always-a-primitive-element-of-textgf2m -> convert from power representation to regular poly representation I've been using so far

power_table = {
    "0": "0",
    "x^0": "1",
    "x^1": "x",
    "x^2": "x^2",
    "x^3": "x^3",
    "x^4": "x+1",
    "x^5": "x^2+x",
    "x^6": "x^3+x^2",
    "x^7": "x^3+x+1",
    "x^8": "x^2+1",
    "x^9": "x^3+x",
    "x^10": "x^2+x+1",
    "x^11": "x^3+x^2+x",
    "x^12": "x^3+x^2+x+1",
    "x^13": "x^3+x^2+1",
    "x^14": "x^3+1",
}

sarkar1_powers = ["x^1", "x^0", "x^4", "x^0", "x^5", "x^14", "x^7", "x^8", "x^3", "x^6", "x^14", "x^14", "x^8", "x^6", "x^3"]
sarkar1_vals = [power_table[i] for i in sarkar1_powers]
#print(sarkar1_vals)
sarkar1_str = toep(sarkar1_vals, 8)
sarkar1 = poly_string_to_integer(sarkar1_str)
get_mat_info_for_mds_table(sarkar1, GF2_4, a.degree, "Sarkar 1")

#% GF(2^8)
#% x^8+x^7+x^6+x+1

b = galois.Poly.Str("x^8+x^7+x^6+x+1", field=GF2)
GF2_8 = galois.GF(2**8, irreducible_poly=b)
#print(GF2_8.properties)

#print(GF2_8.repr_table())

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

#\begin{equation}\label{mat:sarkar-2}
#Toep(1, 1, x, x^{253}, 1, x^{253}, x^{252}, x^{157}, x^{158}, x^{253}, x^{254}, x, x^{254}, x^2, x)
#\end{equation}

sarkar2_powers = ["1", "1", "x", "x^{253}", "1", "x^{253}", "x^{252}", "x^{157}", "x^{158}", "x^{253}", "x^{254}", "x", "x^{254}", "x^2", "x"]
sarkar2_vals = [power_table[i] for i in sarkar2_powers]
#print(sarkar1_vals)
sarkar2_str = toep(sarkar2_vals, 8)
sarkar2 = poly_string_to_integer(sarkar2_str)
get_mat_info_for_mds_table(sarkar2, GF2_8, b.degree, "Sarkar 2")
print("====")
print("sarkar1")
print(sarkar1)
print("sarkar2")
print(sarkar2)