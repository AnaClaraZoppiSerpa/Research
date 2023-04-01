from metrics_and_flags import *

GF2 = galois.GF(2)
a = galois.Poly.Str("x^4 + x + 1", field=GF2)
b = galois.Poly.Str("x^4 + x^3 + x^2 + x + 1", field=GF2)
GF2_4_a = galois.GF(2**4, irreducible_poly=a)
GF2_4_b = galois.GF(2**4, irreducible_poly=b)

print(GF2_4_a.properties)
print("//")
print(GF2_4_b.properties)


