from metrics_and_flags import *

correct_poly = "x^8 + x^4 + x^3 + x^2 + 1" # (GF(2^8), poly)
wrong_poly = "x^8 + x^4 + x^3 + x + 1" # ()

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

GF2 = galois.GF(2)
poly = galois.Poly.Str(correct_poly, field=GF2)
field = galois.GF(2**8, irreducible_poly=poly)

int_to_gf_mat(tavares_mat, field)
get_mat_info_for_mds_table(tavares_mat, field, poly.degree, "tavares")