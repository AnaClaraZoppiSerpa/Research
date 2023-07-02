import math
import pprint
import numpy as np
import decimal

import decimal
import math

def closest_power_of_2(number):
    decimal.getcontext().prec = 100  # Set desired precision
    decimal_number = decimal.Decimal(number)
    power = decimal_number.ln() / decimal.Decimal(math.log(2))
    rounded_power = power.to_integral_value(rounding=decimal.ROUND_HALF_UP)
    return rounded_power
def multiplications_for_the_determinant(z):
    numbers = list(range(1, z+1))
    factorials = [math.factorial(num) for num in numbers]
    return np.prod(factorials, dtype=decimal.Decimal)

def submatrices_removing_k_rows_and_columns(n, k):
    numerator = decimal.Decimal(math.factorial(n))
    denominator = decimal.Decimal(math.factorial(k) * math.factorial(n-k))
    result = (numerator / denominator) ** 2
    return result

def total_amount_of_submatrices_per_k(n):
    total_submats = decimal.Decimal(0)
    per_k = {}
    for k in range(0, n):
        per_k[k] = submatrices_removing_k_rows_and_columns(n, k)
        total_submats += per_k[k]
    return total_submats, per_k

def total_coeff_multiplications(n, per_k):
    total_multiplications = decimal.Decimal(0)
    for k in per_k:
        if n-k != 1:
            total_multiplications += multiplications_for_the_determinant(n-k)
    return total_multiplications

def test(test_n):
    decimal.getcontext().prec = 50  # Set desired precision
    total_submats, per_k_dict = total_amount_of_submatrices_per_k(test_n)
    total_multiplications = total_coeff_multiplications(test_n, per_k_dict)

    print("test_n =", test_n)
    print("total submatrices = ", total_submats)
    print("total coefficient multiplications = ", total_multiplications, "= 2^", closest_power_of_2(total_multiplications))
    print("submatrices per dim = ")
    pprint.pprint(per_k_dict)

for n in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 32, 64]:
    test(n)
