import galois
import numpy as np

gupta_pandey_3 = [
    ["x^3+x^2+1" , "x^2+x+1"   , "x^3+x"      , "x+1"],
    ["x^2+x+1"   , "x^3+x^2+1" , "x+1"        , "x^3+x"],
    ["x^3+x"     , "x+1"       , "x^3+x^2+1"  , "x^2+x+1"],
    ["x+1"       , "x^3+x"     , "x^2+x+1"    , "x^3+x^2+1"],
]

GF2 = galois.GF(2)
a = galois.Poly.Str("x^4 + x + 1", field=GF2)
GF2_4 = galois.GF(2**4, irreducible_poly=a)

denominator = galois.Poly.Str("x+1", field=GF2)
_, denominator_inv, _ = galois.egcd(denominator, a)

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
print(gupta_pandey_3_made_involutory)