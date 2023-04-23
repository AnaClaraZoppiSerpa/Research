from metrics_and_flags import *

gupta_pandey_1 = [
            ["1", "x^3 + x^2 + x + 1", "x^2 + x + 1"],
            ["x^3 + 1", "x^2 + 1", "x^3 + x + 1"],
            ["x^3 + x^2 + 1", "x^2", "x^3 + x^2 + x"]
         ]

gupta_pandey_2 = [
            ["1", "x^2 + x", "x^2 + 1"],
            ["x^2 + x", "1", "x^2"],
            ["x^2 + 1", "x^2", "1"]
         ]

gupta_pandey_3 = [
    ["x^3+x^2+1" , "x^2+x+1"   , "x^3+x"      , "x+1"],
    ["x^2+x+1"   , "x^3+x^2+1" , "x+1"        , "x^3+x"],
    ["x^3+x"     , "x+1"       , "x^3+x^2+1"  , "x^2+x+1"],
    ["x+1"       , "x^3+x"     , "x^2+x+1"    , "x^3+x^2+1"],
]

GF2 = galois.GF(2)
a = galois.Poly.Str("x^4 + x + 1", field=GF2)
GF2_4 = galois.GF(2**4, irreducible_poly=a)
#print(GF2_4.properties)

denominator = galois.Poly.Str("x+1", field=GF2)
_, denominator_inv, _ = galois.egcd(denominator, a)
#print(denominator)
#print(denominator_inv)
#print(denominator * denominator_inv)
#print((denominator * denominator_inv) % a)

def multiply_elements(input_mat, factor):
    rows = len(input_mat)
    cols = len(input_mat[0])

    output_mat = [[0 for j in range(cols)] for i in range(rows)]

    for i in range(rows):
        for j in range(cols):
            element = galois.Poly.Str(input_mat[i][j], field=GF2)
            product = (factor * element) % a
            output_mat[i][j] = product._integer
    
    return output_mat

gupta_pandey_3_made_involutory = multiply_elements(gupta_pandey_3, denominator_inv)
#print(gupta_pandey_3_made_involutory)

gupta_pandey_5 = [
    ["x^3 + x^2", "x^2 + 1", "1"],
    ["x^2 + 1", "x^3 + x + 1  ", "1"],
    ["x^3", "x^3 + x^2 + x + 1", "1"],
]

gupta_pandey_6 = [
    ["x^3", "x^3+1", "x^3+1"],
    ["x^3+x^2+x", "x^3+x^2+x+1", "x^3+x^2+x"],
    ["x^2+x+1", "x^2+x+1", "x^2+x"],
]

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

def gupta_pandey_1_to_6():
    field = GF2_4
    poly_order = a.degree
    matrices = [gupta_pandey_1, gupta_pandey_2, gupta_pandey_3, gupta_pandey_3_made_involutory, gupta_pandey_5, gupta_pandey_6]
    names = ["gupta_pandey_1", "gupta_pandey_2", "gupta_pandey_3", "gupta_pandey_3_made_involutory", "gupta_pandey_5", "gupta_pandey_6"]

    for i in range(6):
        matrix = matrices[i]
        name = names[i]

        integer_version = matrix

        if name != "gupta_pandey_3_made_involutory":
            integer_version = poly_string_to_integer(matrix)

        get_mat_info_for_mds_table(integer_version, field, poly_order, name)

gupta_pandey_1_to_6()

#% GF(2^{16})
#% MDS
#% 8x8
#% Circulant
#% x^16 + x^5 + x^3 + x^2 + 1

#\begin{equation}\label{mat:gupta-pandey-IDEA}
#Circ(1, 1, x^2, 1, x^3, 1+x^2, x, 1+x^3)
#\end{equation}

gupta_pandey_idea = [
    ["1", "1", "x^2", "1", "x^3", "1+x^2", "x", "1+x^3"],
    ["1+x^3", "1", "1", "x^2", "1", "x^3", "1+x^2", "x"],
    ["x", "1+x^3", "1", "1", "x^2", "1", "x^3", "1+x^2"],
    ["1+x^2", "x", "1+x^3", "1", "1", "x^2", "1", "x^3"],
    ["x^3", "1+x^2", "x", "1+x^3", "1", "1", "x^2", "1"],
    ["1", "x^3", "1+x^2", "x", "1+x^3", "1", "1", "x^2"],
    ["x^2", "1", "x^3", "1+x^2", "x", "1+x^3", "1", "1"],
    ["1", "x^2", "1", "x^3", "1+x^2", "x", "1+x^3", "1"],
]

idea_poly = galois.Poly.Str("x^16 + x^5 + x^3 + x^2 + 1", field=GF2)
GF2_16 = galois.GF(2**16, irreducible_poly=idea_poly)

#print(GF2_16.properties)
idea_mat = poly_string_to_integer(gupta_pandey_idea)
get_mat_info_for_mds_table(idea_mat, GF2_16, idea_poly.degree, "Gupta Pandey IDEA")

#% GF(2^4)
#% MDS
#% Circulant
#% Orthogonal
#% x^4+x+1
#% 2x2

#\begin{equation}\label{mat:gupta-pandey-23}
#\begin{bmatrix}
#x & 1+x \\
#1+x & x
#\end{bmatrix}
#\end{equation}

gupta_pandey_23 = [
    ["x", "x+1"],
    ["x+1", "x"]
]

gupta_pandey_23_mat = poly_string_to_integer(gupta_pandey_23)
get_mat_info_for_mds_table(gupta_pandey_23_mat, GF2_4, a.degree, "Gupta Pandey 23")

#% GF(2^8)
#% x^8+x^4+x^3+x+1
#% 3x3
#% Orthogonal
#\begin{equation}\label{mat:gupta-pandey-24-1}
#Circ(x, 1+x^2+x^3+x^4+x^6, x + x^2 + x^3 + x^4 + x^6)
#\end{equation}

gupta_pandey_24_1 = [
    ["x", "1+x^2+x^3+x^4+x^6", "x+x^2+x^3+x^4+x^6"],
    ["x+x^2+x^3+x^4+x^6", "x", "1+x^2+x^3+x^4+x^6"],
    ["1+x^2+x^3+x^4+x^6", "x+x^2+x^3+x^4+x^6", "x"],
]

b = galois.Poly.Str("x^8+x^4+x^3+x+1", field=GF2)
GF2_8 = galois.GF(2**8, irreducible_poly=b)

gupta_pandey_24_1_mat = poly_string_to_integer(gupta_pandey_24_1)
get_mat_info_for_mds_table(gupta_pandey_24_1_mat, GF2_8, b.degree, "Gupta Pandey 24_1")

#% GF(2^8)
#% x^8+x^4+x^3+x+1
#% 6x6
#% Orthogonal
#\begin{equation}\label{mat:gupta-pandey-24-2}
#Circ(1, 1, x, 1+x^2+x^3+x^5+x^6+x^7, x+x^5, x^2+x^3+x^6+x^7)
#\end{equation}

gupta_pandey_24_2 = [
    ["1", "1", "x", "1+x^2+x^3+x^5+x^6+x^7", "x+x^5", "x^2+x^3+x^6+x^7"],
    ["x^2+x^3+x^6+x^7", "1", "1", "x", "1+x^2+x^3+x^5+x^6+x^7", "x+x^5"],
    ["x+x^5", "x^2+x^3+x^6+x^7", "1", "1", "x", "1+x^2+x^3+x^5+x^6+x^7"],
    ["1+x^2+x^3+x^5+x^6+x^7", "x+x^5", "x^2+x^3+x^6+x^7", "1", "1", "x"],
    ["x", "1+x^2+x^3+x^5+x^6+x^7", "x+x^5", "x^2+x^3+x^6+x^7", "1", "1"],
    ["1", "x", "1+x^2+x^3+x^5+x^6+x^7", "x+x^5", "x^2+x^3+x^6+x^7", "1"],
]
gupta_pandey_24_2_mat = poly_string_to_integer(gupta_pandey_24_2)
get_mat_info_for_mds_table(gupta_pandey_24_2_mat, GF2_8, b.degree, "Gupta Pandey 24_2")

def lcirc(row):
	first_row = list(row)
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

# GF(2^8)
# x^8+x^6+x^5+x^2+1
# 5x5
# Left circulant
# Involutory

#\begin{equation}\label{mat:gupta-pandey-31-1}
#l-Circ(1, \alpha, \alpha^7+\alpha^5+\alpha^4+\alpha+1, \alpha^7+\alpha^5+\alpha^4+\alpha^3+\alpha+1, \alpha^3+\alpha)
#\end{equation}

print("==============")

c = galois.Poly.Str("x^8+x^6+x^5+x^2+1", field=GF2) #  x^8 + x^6 + x^5 + x^2 + 1
GF2_8_different_poly = galois.GF(2**8, irreducible_poly=c)

gupta_pandey_31_1_first_row = ["1", "x", "x^7+x^5+x^4+x+1", "x^7+x^5+x^4+x^3+x+1", "x^3+x"]
gupta_pandey_31_1_strings = lcirc(gupta_pandey_31_1_first_row)
gupta_pandey_31_1_mat = poly_string_to_integer(gupta_pandey_31_1_strings)
get_mat_info_for_mds_table(gupta_pandey_31_1_mat, GF2_8_different_poly, c.degree, "Gupta Pandey 31_1")

#for row in gupta_pandey_31_1_strings:
#    print(row)

#% GF(2^8)
#% x^8+x^6+x^5+x^2+1
#% 6x6
#% Left circulant
#% Involutory

#\begin{equation}\label{mat:gupta-pandey-31-2}
#l-Circ(1, 1, \alpha^7+\alpha^5+\alpha^4+\alpha+1, \alpha^5+\alpha^3+\alpha^2, \alpha^2, \alpha^7+\alpha^4+\alpha^3+\alpha)
#\end{equation}

gupta_pandey_31_2_first_row = ["1", "1", "x^7+x^5+x^4+x+1", "x^5+x^3+x^2", "x^2", "x^7+x^4+x^3+x"]
gupta_pandey_31_2_strings = lcirc(gupta_pandey_31_2_first_row)
gupta_pandey_31_2_mat = poly_string_to_integer(gupta_pandey_31_2_strings)
get_mat_info_for_mds_table(gupta_pandey_31_2_mat, GF2_8_different_poly, c.degree, "Gupta Pandey 31_2")

#% GF(2^8)
#% x^8+x^4+x^3+x+1
#% Orthogonal
#% 3x3
#\begin{equation}\label{mat:gupta-pandey-34-1}
#Toep(\alpha, 1+\alpha^2+\alpha^3+\alpha^4+\alpha^6, \alpha+\alpha^2+\alpha^3+\alpha^4+\alpha^6), \alpha+\alpha^2+\alpha^3+\alpha^4+\alpha^6, 1+\alpha^2+\alpha^3+\alpha^4+\alpha^6)
#\end{equation}

# Toeplitz matrices
# arguments: a(0), a(1), ..., a(n-1), a(-1), a(-2), ... a(-(n-1))
# matrix structure: A_(i,j) = a(j-i) 

# toep indexing
# 0, 1, ... , n - 1 : same
# > n-1 : negative
# n -> -1
# n+1 -> -2
# n+2 -> -3

def toep(sequence, n):
    n = len(sequence) // 2
    first_column = sequence[n:]
    first_row = sequence[:n]
    matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if j >= i:
                matrix[i][j] = first_row[j-i]
            else:
                matrix[i][j] = first_column[i-j]
    return matrix

#values = ["a0", "a1", "a2", "a3", "a-1", "a-2", "a-3"]
#toep_test = toep(values, 4)
#print(toep_test)

gp_34_1_vals = ["x", "1+x^2+x^3+x^4+x^6", "x+x^2+x^3+x^4+x^6", "x+x^2+x^3+x^4+x^6", "1+x^2+x^3+x^4+x^6"]
gp_34_1_str = toep(gp_34_1_vals, 3)

#for row in gp_34_1_str:
#    print(row)

gp_34_1_mat = poly_string_to_integer(gp_34_1_str)
get_mat_info_for_mds_table(gp_34_1_mat, GF2_8, b.degree, "Gupta Pandey 34_1")

#% GF(2^8)
#% x^8+x^4+x^3+x+1
#% Orthogonal
#% 6x6
#\begin{align}\label{mat:gupta-pandey-34-2}
#Toep(1,1,\alpha,1+\alpha^2 +\alpha^3 +\alpha^5 +\alpha^6 +\alpha^7, \alpha + \alpha^5, \alpha^2 + \alpha^3 + \alpha^6 + \alpha^7, \alpha^2 + \alpha^3 \nonumber \\ + \alpha^6 + \alpha^7, \alpha + \alpha^5, 1 + \alpha^2 + \alpha^3 + \alpha^5 + \alpha^6 + \alpha^7, \alpha,1)
#\end{align}

gp_34_2_vals = ["1","1","x","1+x^2+x^3+x^5+x^6+x^7", "x+x^5", "x^2+x^3+x^6+x^7", "x^2+x^3+x^6+x^7", "x+x^5", "1+x^2+x^3+x^5+x^6+x^7", "x","1"]
gp_34_2_str = toep(gp_34_2_vals, 6)
gp_34_2_mat = poly_string_to_integer(gp_34_2_str)
get_mat_info_for_mds_table(gp_34_2_mat, GF2_8, b.degree, "Gupta Pandey 34_2")

def hank(values, n):
    A = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            hank_index = i+j
            A[i][j] = values[hank_index]
    return A

#hank_vals = ["a0", "a1", "a2", "a3", "a4"]
#hank_test = hank(hank_vals, 3)
#print(hank_test)

#% GF(2^8)
#% x^8 + x^6 + x^5 + x^2 + 1
#% 5x5
#% Involutory

#\begin{equation}\label{mat:gupta-pandey-36-1}
#Hank(1, \alpha, \alpha^7 +\alpha^5 +\alpha^4 +\alpha+1,\alpha^7 +\alpha^5 +\alpha^4 +\alpha^3 +\alpha+1,\alpha^3 +\alpha, 1,\alpha,\alpha^7 +\alpha^5 +\alpha^4 +\alpha+1, \alpha^7+\alpha^5+\alpha^4+\alpha^3+\alpha+1)
#\end{equation}

gp_36_1_vals = ["1", "x", "x^7+x^5+x^4+x+1", "x^7+x^5+x^4+x^3+x+1","x^3+x", "1","x","x^7+x^5+x^4+x+1", "x^7+x^5+x^4+x^3+x+1"]
gp_36_1_str = hank(gp_36_1_vals, 5)
gp_36_1_mat = poly_string_to_integer(gp_36_1_str)
get_mat_info_for_mds_table(gp_36_1_mat, GF2_8_different_poly, c.degree, "Gupta Pandey 36_1")

#% GF(2^8)
#% x^8 + x^6 + x^5 + x^2 + 1
#% 6x6
#% Involutory

#\begin{equation}\label{mat:gupta-pandey-36-2}
#Hank(1,1,\alpha^7+\alpha^5+\alpha^4+\alpha+1, \alpha^5 +\alpha^3 +\alpha^2,\alpha^2,\alpha^7 +\alpha^4 +\alpha^3 +\alpha, 1,1,\alpha^7 +\alpha^5 +\alpha^4 +\alpha+1,\alpha^5 +\alpha^3 +\alpha^2,\alpha^2)
#\end{equation}

gp_36_2_vals = ["1","1","x^7+x^5+x^4+x+1","x^5+x^3+x^2","x^2","x^7+x^4+x^3+x","1","1","x^7+x^5+x^4+x+1","x^5+x^3+x^2","x^2"]
gp_36_2_str = hank(gp_36_2_vals, 6)
gp_36_2_mat = poly_string_to_integer(gp_36_2_str)
get_mat_info_for_mds_table(gp_36_2_mat, GF2_8_different_poly, c.degree, "Gupta Pandey 36_2")