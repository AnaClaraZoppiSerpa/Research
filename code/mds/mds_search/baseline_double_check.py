from metrics_and_flags import *

GF2 = galois.GF(2)

## 2x2
# Hierocrypt L1

hierocrypt_2x2_field = galois.GF(2**4)

hierocrypt_2x2_l1_mdsh = [
  [0x5, 0x7],
  [0xa, 0xb]
]

## 3x3
# BKSQ
# Curupira
# Curupira key schedule

curupira_poly = galois.Poly([1, 0, 1, 0, 0, 1, 1, 0, 1], field=GF2)
curupira_field = galois.GF(2**8, irreducible_poly=curupira_poly)

curupira_mat = [
    [3, 2, 2],
    [4, 5, 4],
    [6, 6, 7]
]


## 4x4
# Square
# Rijndael
# Anubis, Anubis key schedule
# Hierocrypt-3 and L1, Hierocrypt-3
# FOX
# PHOTON
# LED
# Joltik
# Ref 21
# Ref 36

## 5x5, 6x6, 7x7
# PHOTON

photon_field = galois.GF(2**4)

photon5x5_mat = [
	[1, 2, 9, 9, 2],
	[2, 5, 3, 8, 13],
	[13, 11, 10, 12, 1],
	[1, 15, 2, 3, 14],
	[14, 14, 8, 5, 12]
]

photon6x6_mat = [
	[1, 2, 8, 5, 8, 2],
	[2, 5, 1, 2, 6, 12],
	[12, 9, 15, 8, 8, 13],
	[13, 5, 11, 3, 10, 1],
	[1, 15, 13, 14, 11, 8],
	[8, 2, 3, 3, 2, 8]
]

## 8x8

## 16x16

## 32x32


################################ SHARK ######################################################################

shark_poly = galois.Poly([1, 1, 1, 1, 1, 0, 1, 0, 1], field=GF2)
shark_field = galois.GF(2**8, irreducible_poly=shark_poly)

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

################################ SQUARE ######################################################################

square_poly = galois.Poly([1, 1, 1, 1, 1, 0, 1, 0, 1], field=GF2)
square_field = galois.GF(2**8, irreducible_poly=square_poly)

square_mat = [
		[0x02, 0x01, 0x01, 0x03],
		[0x03, 0x02, 0x01, 0x01],
		[0x01, 0x03, 0x02, 0x01],
		[0x01, 0x01, 0x03, 0x02]
	]

################################ Tavares ######################################################################

################################ BKSQ ######################################################################

################################ Rijndael ######################################################################

################################ KHAZAD ######################################################################

################################ Anubis ######################################################################

################################ Anubis key schedule ######################################################################

################################ Hierocrypt-3 and L1 ######################################################################

################################ Hierocrypt-3 ######################################################################

################################ Hierocrypt L1 ######################################################################

################################ Shirai C0 ######################################################################

################################ Shirai C1 ######################################################################

################################ Shirai C2 ######################################################################

################################ Shirai C3 ######################################################################

################################ Shirai C4 ######################################################################

################################ Shirai C5 ######################################################################

################################ Shirai C6 ######################################################################

################################ Shirai C7 ######################################################################

################################ Shirai C8 ######################################################################

################################ Shirai C9 ######################################################################

################################ Shirai C10 ######################################################################

################################ Shirai C11 ######################################################################

################################ Shirai C12 ######################################################################

################################ Shirai C13 ######################################################################

# Gupta-Ray
# x8+x4+x3+x+1
gupta_ray_poly = galois.Poly([1, 0, 0, 0, 1, 1, 0, 1, 1], field=GF2)
gupta_ray_field = galois.GF(2**8, irreducible_poly=gupta_ray_poly)

gupta_ray_mat_0 = [
    [0x01, 0x02, 0x03, 0xd0],
    [0x02, 0x01, 0xd0, 0x03],
    [0x03, 0xd0, 0x01, 0x02],
    [0xd0, 0x03, 0x02, 0x01],
]
"""
01_x & 02_x & 03_x & d0_x\\
02_x & 01_x & d0_x & 03_x\\
03_x & d0_x & 01_x & 02_x\\
d0_x & 03_x & 02_x & 01_x
"""

gupta_ray_3x3 = [
    [0x7a, 0xf4, 0x8e],
    [0xf4, 0x7a, 0x01],
    [0x8e, 0x01, 0x7a]
]

gupta_ray_example2 = [
    [0x01, 0x02, 0xfc, 0xfe],
    [0x02, 0x01, 0xfe, 0xfc],
    [0xfc, 0xfe, 0x01, 0x02],
    [0xfe, 0xfc, 0x02, 0x01]
]

def ff_hadamard_from_row(first_row):
    n = len(first_row)
    ff_had = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            ff_had[i][j] = first_row[i ^ j]
    return ff_had

gupta_ray_example3 = ff_hadamard_from_row([0x01, 0x02, 0x06, 0x8c, 0x30, 0xfb, 0x87, 0xc4])

"""
1_x & 2_x & 6_x & 8c_x & 30_x & fb_x & 87_x & c4_x\\
2_x & 1_x & 8c_x & 6_x & fb_x & 30_x & c4_x & 87_x\\
6_x & 8c_x & 1_x & 2_x & 87_x & c4_x & 30_x & fb_x\\
8c_x & 6_x & 2_x & 1_x & c4_x & 87_x & fb_x & 30_x\\
30_x & fb_x & 87_x & c4_x & 1_x & 2_x & 6_x & 8c_x\\
fb_x & 30_x & c4_x & 87_x & 2_x & 1_x & 8c_x & 6_x\\
87_x & c4_x & 30_x & fb_x & 6_x & 8c_x & 1_x & 2_x\\
c4_x & 87_x & fb_x & 30_x & 8c_x & 6_x & 2_x & 1_x
"""

gupta_ray_example4 = ff_hadamard_from_row([0x01, 0x03, 0x08, 0xb2, 0x0d, 0x60, 0xe8, 0x1c, 0x0f, 0x2c, 0xa2, 0x8b, 0xc9, 0x7a, 0xac, 0x35])

gupta_ray_example5 = ff_hadamard_from_row([0x01, 0x02, 0x04, 0x69, 0x07, 0xec, 0xcc, 0x72, 0x0b, 0x54, 0x29, 0xbe, 0x74, 0xf9, 0xc4, 0x87, 0x0e, 0x47, 0xc2, 0xc3, 0x39, 0x8e, 0x1c, 0x85, 0x55, 0x26, 0x1e, 0xaf, 0x68, 0xb6, 0x59, 0x1f])

sim_khoo_poly_0x13 = galois.Poly([1, 0, 0, 1, 1], field=GF2)
sim_khoo_field_gf4_0x13 = galois.GF(2**4, irreducible_poly=sim_khoo_poly_0x13)

sim_khoo_poly_0x19 = galois.Poly([1,1,0,0,1], field=GF2)
sim_khoo_field_gf4_0x19 = galois.GF(2**4, irreducible_poly=sim_khoo_poly_0x19)

sim_khoo_poly_0x165 = galois.Poly([1,0,1,1,0,0,1,0,1], field=GF2)
sim_khoo_field_gf8_0x165 = galois.GF(2**8, irreducible_poly=sim_khoo_poly_0x165)

sim_khoo_poly_0x1c3 = galois.Poly([1,1,1,0,0,0,0,1,1], field=GF2)
sim_khoo_field_gf8_0x1c3 = galois.GF(2**8, irreducible_poly=sim_khoo_poly_0x1c3)

sim_khoo_pg10 = ff_hadamard_from_row([15, 2, 12, 5, 10, 4, 3, 8])
sim_khoo_157 = ff_hadamard_from_row([0x1, 0x4, 0x9, 0xd])
sim_khoo_158 = ff_hadamard_from_row([0x01, 0x02, 0xb0, 0xb2])
sim_khoo_159 = ff_hadamard_from_row([0x01, 0x02, 0x03, 0x91, 0x04, 0x70, 0x05, 0xe1])
sim_khoo_160 = ff_hadamard_from_row([0x2, 0x3, 0x4, 0xc, 0x5, 0xa, 0x8, 0xf])
sim_khoo_161 = ff_hadamard_from_row([0x08, 0x16, 0x8a, 0x01, 0x70, 0x8d, 0x24, 0x76, 0xa8, 0x91, 0xad, 0x48, 0x05, 0xb5, 0xaf, 0xf8])
sim_khoo_162 = ff_hadamard_from_row([0xd2, 0x06, 0x05, 0x4d, 0x21, 0xf8, 0x11, 0x62, 0x08, 0xd8, 0xe9, 0x28, 0x4b, 0xa6, 0x10, 0x2c,
0xa1, 0x49, 0x4c, 0xd1, 0x59, 0xb2, 0x13, 0xa4, 0x03, 0xc3, 0x42, 0x79, 0xa0, 0x6f, 0xab, 0x41])

sim_khoo_163 = ff_hadamard_from_row([0x1, 0x2, 0x8, 0x9])
sim_khoo_165 = ff_hadamard_from_row([0x01, 0x02, 0x04, 0x91])
sim_khoo_167 = ff_hadamard_from_row([0x01, 0x02, 0x03, 0x08, 0x04, 0x91, 0xe1, 0xa9])
sim_khoo_169 = ff_hadamard_from_row([0x1, 0x2, 0x6, 0x8, 0x9, 0xc, 0xd, 0xa])
sim_khoo_171 = ff_hadamard_from_row([0xb1, 0x1c, 0x30, 0x09, 0x08, 0x91, 0x18, 0xe4, 0x98, 0x12, 0x70, 0xb5, 0x97, 0x90, 0xa9, 0x5b])

sim_khoo_173 = ff_hadamard_from_row([0xb9, 0x7c, 0x93, 0xbc, 0xbd, 0x26, 0xfa, 0xa9, 0x32, 0x31, 0x24, 0xb5, 0xbb, 0x06, 0xa0, 0x44, 0x95, 0xb3, 0x0c, 0x1c, 0x07, 0xe5, 0xa4, 0x2e, 0x56, 0x4c, 0x55, 0x02, 0x66, 0x39, 0x48, 0x08])

sim_khoo_174 = ff_hadamard_from_row([1,2,6,4])

sim_khoo_175 = ff_hadamard_from_row([0x2, 0x3, 0x4, 0xc, 0x5, 0xa, 0x8, 0xf])

########### Liu Sim ########################################################## 

liu_sim_poly_0x1c3 = galois.Poly.Int(0x1c3, field=GF2)
liu_sim_field_gf256_0x1c3 = galois.GF(2**8, irreducible_poly=liu_sim_poly_0x1c3)

liu_sim_poly_0x11b = galois.Poly.Int(0x11b, field=GF2)
liu_sim_field_gf256_0x11b = galois.GF(2**8, irreducible_poly=liu_sim_poly_0x11b)

liu_sim_poly_0x11d = galois.Poly.Int(0x11d, field=GF2)
liu_sim_field_gf256_0x11d = galois.GF(2**8, irreducible_poly=liu_sim_poly_0x11d)

liu_sim_poly_0x169 = galois.Poly.Int(0x169, field=GF2)
liu_sim_field_gf256_0x169 = galois.GF(2**8, irreducible_poly=liu_sim_poly_0x169)

liu_sim_poly_0x165 = galois.Poly.Int(0x165, field=GF2)
liu_sim_field_gf256_0x165 = galois.GF(2**8, irreducible_poly=liu_sim_poly_0x165)

liu_sim_poly_0x139 = galois.Poly.Int(0x139, field=GF2)
liu_sim_field_gf256_0x139 = galois.GF(2**8, irreducible_poly=liu_sim_poly_0x139)

liu_sim_poly_0x13 = galois.Poly.Int(0x13, field=GF2)
liu_sim_field_gf16_0x13 = galois.GF(2**4, irreducible_poly=liu_sim_poly_0x13)

liu_sim_poly_0x1f = galois.Poly.Int(0x1f, field=GF2)
liu_sim_field_gf16_0x1f = galois.GF(2**4, irreducible_poly=liu_sim_poly_0x1f)

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

# GF((2^8))
# 0x1c3

mat_liu_sim_1 = lcirc((0x01, 0x01, 0x02))
mat_liu_sim_2 = lcirc((0x01, 0x01, 0x02, 0x91))
mat_liu_sim_3 = lcirc((0x01, 0x01, 0x02, 0x91, 0x02))
mat_liu_sim_4 = lcirc((0x01, 0x02, 0xe1, 0x91, 0x01, 0x08))
mat_liu_sim_5 = lcirc((0x01, 0x01, 0x91, 0x02, 0x04, 0x02, 0x91))
mat_liu_sim_6 = lcirc((0x01, 0x01, 0x02, 0xe1, 0x08, 0xe0, 0x01, 0xa9))

# GF((2^4))
# 0x13

mat_liu_sim_7 = lcirc((1, 1, 2))
mat_liu_sim_8 = lcirc((1, 1, 9, 4))
mat_liu_sim_9 = lcirc((2, 2, 9, 1, 9))
mat_liu_sim_10 = lcirc((1, 1, 9, 0xc, 9, 3))

# 0x1c3
mat_liu_sim_11 = lcirc((0x01, 0x01, 0x91, 0x02, 0x04, 0x02, 0x12, 0x91))
mat_liu_sim_12 = lcirc((0x01, 0x01, 0x04, 0x02, 0xa9, 0x91, 0x02, 0x03))
mat_liu_sim_13 = lcirc((0x01, 0x01, 0x02, 0xe0, 0x06, 0xe1, 0x91, 0x04))
mat_liu_sim_14 = lcirc((0x01, 0x02, 0x91, 0x08, 0x04, 0x06, 0xe1, 0x03))

current_poly = liu_sim_poly_0x1c3
current_field = liu_sim_field_gf256_0x1c3
mats_liu_sim = [
	(mat_liu_sim_11,11),
	(mat_liu_sim_12,12),
	(mat_liu_sim_13,13),
	(mat_liu_sim_14,14),
]

for m in mats_liu_sim:
	#print("mat_liu_sim_", m[1])
	#print_mat_hex(m[0])
	get_mat_info_for_mds_table(m[0], current_field, current_poly.degree, "mat_liu_sim_"+str(m[1]))

# 0x11b
mat_liu_sim_15 = lcirc((0x01, 0x01, 0x02, 0x01, 0x74, 0x8d, 0x46, 0x04))

# 0x11d
mat_liu_sim_16 = lcirc((0x01, 0x01, 0x02, 0x8e, 0x47, 0x10, 0x01, 0x46))

# Involutory

# GF((2^8))

# 0x169
mat_liu_sim_17 = lcirc((0x5a, 0x0a, 0x51))

# 0x165
mat_liu_sim_18 = lcirc((0x01, 0x02, 0xb3, 0xbb, 0x0a))
mat_liu_sim_19 = lcirc((0x01, 0x01, 0xb3, 0x2c, 0x04, 0x9a))
mat_liu_sim_20 = lcirc((0x01, 0x02, 0x10, 0xb2, 0x58, 0xa4, 0x5c))

# 0x139
mat_liu_sim_21 = lcirc((0x01, 0x01, 0x21, 0x08, 0x96, 0x26, 0x98))

# GF((2^4))

# 0x1f
mat_liu_sim_22 = lcirc((2, 0xf, 0xc))

# 0x13
mat_liu_sim_23 = lcirc((1, 2, 5, 4, 3))

#get_mat_info_for_mds_table(sim_khoo_175, sim_khoo_field_gf4_0x13, sim_khoo_poly_0x13.degree, "Sim Khoo 175")
#get_mat_info_for_mds_table(sim_khoo_174, sim_khoo_field_gf4_0x19, sim_khoo_poly_0x19.degree, "Sim Khoo 174")
#get_mat_info_for_mds_table(sim_khoo_173, sim_khoo_field_gf8_0x1c3, sim_khoo_poly_0x1c3.degree, "Sim Khoo 173")
#get_mat_info_for_mds_table(sim_khoo_171, sim_khoo_field_gf8_0x1c3, sim_khoo_poly_0x1c3.degree, "Sim Khoo 171")
#get_mat_info_for_mds_table(sim_khoo_169, sim_khoo_field_gf4_0x13, sim_khoo_poly_0x13.degree, "Sim Khoo 169")
#get_mat_info_for_mds_table(sim_khoo_165, sim_khoo_field_gf8_0x1c3, sim_khoo_poly_0x1c3.degree, "Sim Khoo 165")
#get_mat_info_for_mds_table(sim_khoo_163, sim_khoo_field_gf4_0x13, sim_khoo_poly_0x13.degree, "Sim Khoo 163")
#get_mat_info_for_mds_table(sim_khoo_162, sim_khoo_field_gf8_0x165, sim_khoo_poly_0x165.degree, "Sim Khoo 162")
#get_mat_info_for_mds_table(sim_khoo_161, sim_khoo_field_gf8_0x1c3, sim_khoo_poly_0x1c3.degree, "Sim Khoo 161")
#get_mat_info_for_mds_table(sim_khoo_160, sim_khoo_field_gf4_0x13, sim_khoo_poly_0x13.degree, "Sim Khoo 160")
#get_mat_info_for_mds_table(sim_khoo_159, sim_khoo_field_gf8_0x1c3, sim_khoo_poly_0x1c3.degree, "Sim Khoo 159")
#get_mat_info_for_mds_table(sim_khoo_158, sim_khoo_field_gf8_0x165, sim_khoo_poly_0x165.degree, "Sim Khoo 158")
#get_mat_info_for_mds_table(sim_khoo_157, sim_khoo_field_gf4_0x13, sim_khoo_poly_0x13.degree, "Sim Khoo 157")
#get_mat_info_for_mds_table(sim_khoo_pg10, sim_khoo_field, sim_khoo_poly.degree, "Sim Khoo pg 10")
#get_mat_info_for_mds_table(gupta_ray_example5, gupta_ray_field, gupta_ray_field.irreducible_poly.degree, "Gupta Ray Example 4")
#get_mat_info_for_mds_table(gupta_ray_example4, gupta_ray_field, gupta_ray_field.irreducible_poly.degree, "Gupta Ray Example 4")
#get_mat_info_for_mds_table(gupta_ray_example3, gupta_ray_field, gupta_ray_field.irreducible_poly.degree, "Gupta Ray Example 3")
#get_mat_info_for_mds_table(gupta_ray_example2, gupta_ray_field, gupta_ray_field.irreducible_poly.degree, "Gupta Ray Example 2")
#get_mat_info_for_mds_table(gupta_ray_3x3, gupta_ray_field, gupta_ray_field.irreducible_poly.degree, "Gupta Ray 3x3 Mat From Example 1")
#get_mat_info_for_mds_table(gupta_ray_mat_0, gupta_ray_field, gupta_ray_field.irreducible_poly.degree, "Gupta Ray Non Inv Mat From Example 1")
#get_mat_info_for_mds_table(hierocrypt_2x2_l1_mdsh, hierocrypt_2x2_field, hierocrypt_2x2_field.irreducible_poly.degree, "Hierocrypt L1 2x2")
#get_mat_info_for_mds_table(curupira_mat, curupira_field, curupira_field.irreducible_poly.degree, "Curupira (3x3 cheapest, involutory)")
#get_mat_info_for_mds_table(photon5x5_mat, photon_field, photon_field.irreducible_poly.degree, "PHOTON only 5x5")
#get_mat_info_for_mds_table(photon6x6_mat, photon_field, photon_field.irreducible_poly.degree, "PHOTON only 6x6")