from metrics_and_flags import *

# List of fields
## GF(2^2)
## GF(2^3)
## GF(2^4)
## GF(2^5)
## GF(2^6)
## ...
## GF(2^8)

# Minimal list of fields
## GF(2^2)
## GF(2^4)
## GF(2^8)

def print_test_results(test_results):
    for tuple in test_results:
        print(tuple)

GF2 = galois.GF(2)
GF2_2 = galois.GF(2**2)
GF2_4 = galois.GF(2**4)
GF2_8 = galois.GF(2**8)

GF2_3 = galois.GF(2**3)
GF2_5 = galois.GF(2**5)
GF2_6 = galois.GF(2**6)
GF2_7 = galois.GF(2**7)
GF2_9 = galois.GF(2**9)
GF2_10 = galois.GF(2**10)
GF2_11 = galois.GF(2**11)
GF2_12 = galois.GF(2**12)
GF2_13 = galois.GF(2**13)
GF2_14 = galois.GF(2**14)
GF2_15 = galois.GF(2**15)
GF2_16 = galois.GF(2**16)

min_test_fields = [GF2_2, GF2_4, GF2_8]
min_test_degrees = [2, 4, 8]

other_test_fields = [GF2_3, GF2_5, GF2_6, GF2_7] 
other_test_fields_bigger = [GF2_9, GF2_10, GF2_11, GF2_12, GF2_13, GF2_14, GF2_15, GF2_16]

other_test_degrees = [3,5,6,7]
other_test_degrees_bigger = [9,10,11,12,13,14,15,16]

def is_matrix_valid_for_field(matrix, valid_scalar_max):
    for row in matrix:
        for element in row:
            if element > valid_scalar_max:
                return False
    return True

def test_duwal_matrix(int_mat, mat_name, test_fields, test_degrees):
    results = []

    index = 0
    number_of_tests = len(test_fields)
    while index < number_of_tests:
        field = test_fields[index]
        degree = test_degrees[index]
        irreducible_polys = list(galois.irreducible_polys(2, degree))

        valid_scalar_max = 2**degree

        if is_matrix_valid_for_field(int_mat, valid_scalar_max):
            for poly in irreducible_polys:
                print("(testing for field=", str(field), "poly=", str(poly), ")")
                is_mds_mat, is_mds_inv, xr, xt, ixr, ixt = get_mat_info_for_mds_table(int_mat, field, degree, mat_name)
                results.append((mat_name, str(field), str(poly), is_mds_mat, is_mds_inv, xr, xt, ixr, ixt))
        else:
            results.append((mat_name, str(field), "invalid because elements are bigger than the max"))

        index += 1
    return results

def minimal_test(int_mat, mat_name):
    test_results = test_duwal_matrix(int_mat, mat_name, min_test_fields, min_test_degrees)
    print("[ TEST RESULTS FOR", mat_name, " ]")
    print_test_results(test_results)

def smaller_test(int_mat, mat_name):
    test_results = test_duwal_matrix(int_mat, mat_name, other_test_fields, other_test_degrees)
    print("[ TEST RESULTS FOR", mat_name, " ]")
    print_test_results(test_results)

def bigger_test(int_mat, mat_name):
    test_results = test_duwal_matrix(int_mat, mat_name, other_test_fields_bigger, other_test_degrees_bigger)
    print("[ TEST RESULTS FOR", mat_name, " ]")
    print_test_results(test_results)

#print(GF2_4.properties)
#polys = list(galois.irreducible_polys(2, 4))
#for poly in polys:
#    print(poly)

#% Duwal

#The following matrices have been reported by Duval and Leurent \cite{LwCircuits2018}.

#% GF(2^2)
#% x^2+x+1

duwal_1_int = [[2, 1, 1],[1, 2, 1],[1, 1, 2]]
duwal_2_int = [[3, 2, 2],[2, 3, 2],[2, 2, 3]]

#% GF(2^3) eu acho, por causa do textinho da seção 5 (Results) que fala k = 3 e F_2^k. Tem que ver qual o polinômio irredutível só.

duwal_3_int = [[2, 1, 3],[1, 1, 1],[3, 1, 2]]
duwal_3_inv_int = [[3, 1, 2],[1, 1, 1],[2, 1, 3]]
duwal_4_int = [[3, 1, 3],[1, 1, 2],[2, 1, 1]]
duwal_5_int = [[2, 1, 1],[1, 2, 1],[1, 1, 2]]

#% Table 4
#% GF(2^4) pras que têm número, NA pras outras porque pode instanciar com outro k aparentemente
#% O que é alfa, beta, gama?
#% alfa é x, beta é x^(k+1), gama é x^(k+1)^2 - confirmar isso aqui

duwal_6_int = [[2, 2, 3, 1], [1, 3, 6, 4],[3, 1, 4, 4],[3, 2, 1, 3]]

def ffsum(a, b):
    pass

def ffsum3(a, b, c):
    pass

alpha=0
gamma=0
beta=0

duwal_7 = [
    [beta, 1, beta+1, 1],
    [gamma, alpha, gamma, ffsum(alpha,1)],
    [gamma, ffsum(alpha,1), ffsum(gamma,1), ffsum3(alpha,gamma,1)],
    [ffsum(beta,gamma), 1, ffsum3(beta,gamma,1), ffsum(gamma,1)]
    ]

duwal_8_int = [[2, 2, 3, 1],[1, 3, 6, 4],[3, 1, 4, 4],[3, 2, 1, 3]]
duwal_9_int = [[5, 7, 1, 3],[4, 6, 1, 1],[1, 3, 5, 7],[1, 1, 4, 6]]
duwal_10_int = [[6, 7, 1, 5],[2, 3, 1, 1],[1, 5, 6, 7],[1, 1, 2, 3]]
duwal_11_int = [[3, 2, 1, 3],[2, 3, 1, 1],[4, 3, 6, 4],[1, 1, 4, 6]]

alpha=0
gamma=0
beta=0

duwal_12 = [
    [ffsum(alpha,1), alpha, ffsum(gamma,1), ffsum(gamma,1)],
    [beta, ffsum(beta,1), 1, beta],
    [1, 1, gamma, ffsum(gamma,1)],
    [alpha, ffsum(alpha,1), ffsum(gamma,1), gamma]
    ]

duwal_13_int = [[1, 2, 4, 3],[2, 3, 2, 3],[3, 3, 5, 1],[3, 1, 1, 3]]

alpha=0
gamma=0
beta=0
alphainv=0

duwal_14 = [
    [ffsum(alpha,alphainv), alpha, 1, 1],
    [1, ffsum(alpha,1), alpha, alphainv],
    [ffsum(1,alphainv), 1, 1, ffsum(1,alphainv)],
    [alphainv, alphainv, ffsum(1,alphainv), 1]
    ]

int_mats_and_names = [
    (duwal_1_int, "duwal_1_int"),
    (duwal_2_int, "duwal_2_int"),
    (duwal_3_int, "duwal_3_int"),
    (duwal_3_inv_int, "duwal_3_inv_int"),
    (duwal_4_int, "duwal_4_int"),
    (duwal_5_int, "duwal_5_int"),
    (duwal_6_int, "duwal_6_int"),
    (duwal_13_int, "duwal_13_int"),
    ]

for pair in int_mats_and_names:
    #minimal_test(pair[0], pair[1]) # DONE!
    #smaller_test(pair[0], pair[1]) # DONE!
    bigger_test(pair[0], pair[1])