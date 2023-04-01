from metrics_and_flags import *

GF2 = galois.GF(2)
GF2_2 = galois.GF(2**2)
GF2_4 = galois.GF(2**4)
GF2_8 = galois.GF(2**8)

field = galois.GF(2**4)

print(field.properties)
print(field.repr_table())

print(field.arithmetic_table("*"))

a = galois.Poly.Int(2, field=field) # a -> alfa
b = galois.Poly.Int(9, field=field) # b -> beta = alfa^-1
y = galois.Poly.Int(4, field=field) # y -> gamma = alfa^2
i = galois.Poly.Int(1, field=field) # 1 as a polynomial object

duwal_7 = [
    [b, i, b+i, i],
    [y, a, y, a+y],
    [y, a+i, y+i, a+y+i],
    [b+y, i, b+y+i, y+i]
]

for row in duwal_7:
    print(row)

duwal_7_with_ints = [
    [9, 1, 8, 1],
    [4, 2, 4, 6],
    [4, 3, 5, 7],
    [13, 1, 12, 5]
]

get_mat_info_for_mds_table(duwal_7_with_ints, GF2_4, 4, "duwal_7")

