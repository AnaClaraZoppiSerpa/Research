import galois

polys = [
    '13',
    '1f',
    '139',
    '165',
    '169',
    '11d',
    '11b',
    '1c3',
]

for p in polys:
    integer = int(p, 16)
    poly = galois.Poly.Int(integer)
    print(p, integer, bin(integer), poly)