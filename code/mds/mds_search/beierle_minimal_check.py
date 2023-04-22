# beierle_2x2 - OK
# beierle_2x2_inv - OK
# beierle_3x3 - OK
# beierle_3x3_inv - OK
# beierle_4x4 - OK
# beierle_5x5 - OK
# beierle_6x6 - OK
# beierle_7x7 - OK
# beierle_8x8 - OK

from metrics_and_flags import *

GF2 = galois.GF(2)
GF2_4 = galois.GF(2**4)
GF2_8 = galois.GF(2**8)

GLOBAL_RESULTS_LIST = []

def pposs(poss_list):
	for tuple in poss_list:
		alpha = tuple[0]
		gf_mat = tuple[1]
		int_mat = tuple[2]

		print("alpha = ", alpha)
		pmat(int_mat)

def pmat(m):
	for r in m:
		print(r)

def info(mat, name):
	print(GF2_4.properties)
	res1 = (name,"GF2_4") + get_mat_info_for_mds_table(mat, GF2_4, GF2_4.irreducible_poly.degree, name)
	
	print(GF2_8.properties)
	res2 = (name,"GF2_8") + get_mat_info_for_mds_table(mat, GF2_8, GF2_8.irreducible_poly.degree, name)

	GLOBAL_RESULTS_LIST.append(res1)
	GLOBAL_RESULTS_LIST.append(res2)

def info_f(mat, name, F, F_str):
	print(F.properties)
	res1 = (name,F_str) + get_mat_info_for_mds_table(mat, F, F.irreducible_poly.degree, name)
	GLOBAL_RESULTS_LIST.append(res1)

def circ(first_row):
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

# alpha != 0, 1 -> alpha >= 2
beierle_2x2=[
    [1, 2],
    [2, 1],
]

# alpha != 0, 1 -> alpha >= 2
beierle_3x3=[
    [1, 1, 2],
    [2, 1, 1],
    [1, 2, 1],
]

def testing_negative_alpha():
	alpha = 2
	while alpha <= 16:
		alpha_gf = galois.Poly.Int(alpha)
		neg_alpha_gf = -alpha_gf
		print(alpha_gf, neg_alpha_gf)
		alpha+=1

def beierle_2x2_inv_possibilities(F):
	"""
	\begin{equation}\label{mat:beierle-2x2-inv}
	\frac{1}{1-\alpha^2} \cdot
	\begin{bmatrix}
	1 & -\alpha\\
	-\alpha & 1
	\end{bmatrix}
	\end{equation}
	"""
	possibilities = []

	min_alpha = 1
	max_alpha = 2**F.irreducible_poly.degree - 1

	alpha = min_alpha
	while alpha <= max_alpha:
		alpha_gf = galois.Poly.Int(alpha)
		neg_alpha_gf = -alpha_gf
		alpha_sq = (alpha_gf**2) % F.irreducible_poly
		gf_1 = galois.Poly.Int(1)
		denominator = gf_1 - alpha_sq
		_, frac, _ = galois.egcd(denominator, F.irreducible_poly)

		matrix = [
			[frac, (neg_alpha_gf * frac) % F.irreducible_poly],
			[(neg_alpha_gf * frac) % F.irreducible_poly, frac]
		]
		int_ver = gf_to_int(matrix)
		
		mat_tuple = (alpha, matrix, int_ver)
		possibilities.append(mat_tuple)

		alpha += 1
	
	return possibilities

"""
\begin{equation}\label{mat:beierle-3x3-inv}
\frac{1}{(1-\alpha)-(\alpha-1)+\alpha(\alpha^2-1)} \cdot
\begin{bmatrix}
1-\alpha & \alpha^2-1 & 1-\alpha \\
1-\alpha & 1-\alpha & \alpha^2-1 \\
\alpha^2-1 & 1-\alpha & 1-\alpha
\end{bmatrix}
\end{equation}
"""

def beierle_3x3_inv_possibilities(F):
	possibilities = []

	min_alpha = 1
	max_alpha = 2**F.irreducible_poly.degree - 1

	alpha = min_alpha
	while alpha <= max_alpha:
		alpha_gf = galois.Poly.Int(alpha)
		alpha_sq = (alpha_gf ** 2) % F.irreducible_poly
		gf_1 = galois.Poly.Int(1)
		prod = (alpha_gf * (alpha_sq - gf_1)) % F.irreducible_poly
		den = gf_1 - alpha_gf - (alpha_gf - gf_1) + prod
		_, frac, _ = galois.egcd(den, F.irreducible_poly)

		m1 = ((gf_1 - alpha_gf) * frac) % F.irreducible_poly
		m2 = ((alpha_sq - gf_1) * frac) % F.irreducible_poly
		m3 = ((gf_1 - alpha_gf) * frac) % F.irreducible_poly
		m4 = m1
		m5 = m1
		m6 = m2
		m7 = m2
		m8 = m1
		m9 = m1
		
		matrix = [
			[m1, m2, m3],
			[m4, m5, m6],
			[m7, m8, m9]
		]
		int_ver = gf_to_int(matrix)
		
		mat_tuple = (alpha, matrix, int_ver)
		possibilities.append(mat_tuple)

		alpha += 1
	
	return possibilities

def gf_to_int(gf_mat):
    rows = len(gf_mat)
    cols = len(gf_mat[0])

    int_mat = [[0 for i in range(rows)] for j in range(cols)]

    for i in range(rows):
        for j in range(cols):
            int_mat[i][j] = gf_mat[i][j]._integer

    return int_mat

def beierle_4x4_possibilities(F):
	possibilities = []

	min_alpha = 1
	max_alpha = 2**F.irreducible_poly.degree - 1

	alpha = min_alpha
	while alpha <= max_alpha:
		alpha_gf = galois.Poly.Int(alpha)
		gf_1 = galois.Poly.Int(1)
		_, alpha_inv, _ = galois.egcd(alpha_gf, F.irreducible_poly)
		alpha_pow_gf = (alpha_inv**2 % F.irreducible_poly)

		if alpha_pow_gf != galois.Poly.Int(0):
			matrix = circ([gf_1, gf_1, alpha_gf, alpha_pow_gf]) #TODO: change for each matrix!
			int_ver = gf_to_int(matrix)
			
			mat_tuple = (alpha, matrix, int_ver)
			possibilities.append(mat_tuple)

		alpha += 1
	
	return possibilities

def beierle_5x5_possibilities(F):
	possibilities = []

	min_alpha = 1
	max_alpha = 2**F.irreducible_poly.degree - 1

	alpha = min_alpha
	while alpha <= max_alpha:
		alpha_gf = galois.Poly.Int(alpha)
		gf_1 = galois.Poly.Int(1)
		_, alpha_inv, _ = galois.egcd(alpha_gf, F.irreducible_poly)
		alpha_pow_gf = (alpha_inv**2 % F.irreducible_poly)

		if alpha_pow_gf != galois.Poly.Int(0):
			matrix = circ([gf_1, gf_1, alpha_gf, alpha_pow_gf, alpha_gf]) #TODO: change for each matrix!
			int_ver = gf_to_int(matrix)
			
			mat_tuple = (alpha, matrix, int_ver)
			possibilities.append(mat_tuple)

		alpha += 1
	
	return possibilities

def beierle_6x6_possibilities(F):
	possibilities = []

	min_alpha = 1
	max_alpha = 2**F.irreducible_poly.degree - 1

	alpha = min_alpha
	while alpha <= max_alpha:
		alpha_gf = galois.Poly.Int(alpha)
		gf_1 = galois.Poly.Int(1)
		_, alpha_inv, _ = galois.egcd(alpha_gf, F.irreducible_poly)
		alpha_pow_gf = (alpha_inv**2 % F.irreducible_poly)
		alpha_gf_cube = alpha_gf**3 % F.irreducible_poly

		if alpha_pow_gf != galois.Poly.Int(0):
			# 1, \alpha, \alpha^{-1}, \alpha^{-2}, 1, \alpha^3
			matrix = circ([gf_1, alpha_gf, alpha_inv, alpha_pow_gf, gf_1, alpha_gf_cube]) #TODO: change for each matrix!
			int_ver = gf_to_int(matrix)
			
			mat_tuple = (alpha, matrix, int_ver)
			possibilities.append(mat_tuple)

		alpha += 1
	
	return possibilities

def beierle_7x7_possibilities(F):
	possibilities = []

	min_alpha = 1
	max_alpha = 2**F.irreducible_poly.degree - 1

	alpha = min_alpha
	while alpha <= max_alpha:
		alpha_gf = galois.Poly.Int(alpha)
		gf_1 = galois.Poly.Int(1)
		_, alpha_inv, _ = galois.egcd(alpha_gf, F.irreducible_poly)
		alpha_pow_gf = (alpha_inv**2 % F.irreducible_poly)
		alpha_gf_cube = alpha_gf**3 % F.irreducible_poly
		alpha_gf_square = alpha_gf**2 % F.irreducible_poly

		if alpha_pow_gf != galois.Poly.Int(0):
			# circ(1*, 1*, \alpha^{-2}*, \alpha*, \alpha^2*, \alpha*, \alpha^{-2}*)
			matrix = circ([gf_1, gf_1, alpha_pow_gf, alpha_gf, alpha_gf_square, alpha_gf, alpha_pow_gf]) #TODO: change for each matrix!
			int_ver = gf_to_int(matrix)
			
			mat_tuple = (alpha, matrix, int_ver)
			possibilities.append(mat_tuple)

		alpha += 1
	
	return possibilities

def beierle_8x8_possibilities(F):
	possibilities = []

	min_alpha = 1
	max_alpha = 2**F.irreducible_poly.degree - 1

	alpha = min_alpha
	while alpha <= max_alpha:
		alpha_gf = galois.Poly.Int(alpha)
		gf_1 = galois.Poly.Int(1)
		_, alpha_inv, _ = galois.egcd(alpha_gf, F.irreducible_poly)
		
		alpha_gf_cube = alpha_gf**3 % F.irreducible_poly
		alpha_gf_pow4 = alpha_gf**4 % F.irreducible_poly
		alpha_inv_gf_cube = alpha_inv**3 % F.irreducible_poly

		# circ(1*, 1*, \alpha^{-1}*, \alpha*, \alpha^{-1}*, \alpha^3*, \alpha^{4}*, \alpha^{-3}*)
		matrix = circ([gf_1, gf_1, alpha_inv, alpha_gf, alpha_inv, alpha_gf_cube, alpha_gf_pow4, alpha_inv_gf_cube]) #TODO: change for each matrix!
		int_ver = gf_to_int(matrix)
		
		mat_tuple = (alpha, matrix, int_ver)
		possibilities.append(mat_tuple)

		alpha += 1
	
	return possibilities

Fs = [(GF2_4,"GF2_4"),
      (GF2_8,"GF2_8")]

def get_results(mat_function, id):
	for f in Fs:
		poss = mat_function(f[0])

		for p in poss:
			alpha = p[0]
			gf_mat = p[1]
			int_mat = p[2]

			mat_id = id+"_alpha_"+str(alpha)
			print(mat_id)
			info_f(int_mat, mat_id, f[0], f[1])

info(beierle_2x2, "beierle_2x2")
info(beierle_3x3, "beierle_3x3")
get_results(beierle_2x2_inv_possibilities, "beierle_2x2_inv")
get_results(beierle_3x3_inv_possibilities, "beierle_3x3_inv")
get_results(beierle_4x4_possibilities, "beierle_4x4")
get_results(beierle_5x5_possibilities, "beierle_5x5")
get_results(beierle_6x6_possibilities, "beierle_6x6")
get_results(beierle_7x7_possibilities, "beierle_7x7")
get_results(beierle_8x8_possibilities, "beierle_8x8")

#testing_negative_alpha()

print("============")
for r in GLOBAL_RESULTS_LIST:
	print(r)
