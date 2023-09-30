import math
from typing import List, Any


def is_factor(number):
    factors = []
    i = 1
    while i * i <= number:
        if number % i == 0:
            factors.append(int(i))
            if number / i != i:
                factors.append(int(number / i))
        i += 1
    factors.sort()
    return factors


def is_number_prime(number):
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


initial_number = 600851475143
prime_factor = []
factor_list = is_factor(initial_number)



for i in factor_list:
    if is_number_prime(i):
        prime_factor.append(i)

print(max(prime_factor))

