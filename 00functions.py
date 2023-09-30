import math as m
"""
check prime funtion (works, long list)
check = 25


def is_number_prime(number):
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True



for n in range(2,check):
    print(n, is_number_prime(n))
"""

"""
def is_factor(number):
    factor_list = []
    i = 1
    while i * i <= number:
        if number % i == 0:
            factor_list.append(i)
            if number / i != i:
                factor_list.append(number/i)
        i += 1

    return factor_list


print(is_factor(600851475143))
"""


