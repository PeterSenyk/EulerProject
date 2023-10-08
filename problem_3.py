import math


def is_factor(number):
    factors = []
    for factor in range(2, math.ceil(math.sqrt(number))):
        if number % factor == 0:
            factors.append(int(factor))
            if number / factor != factor:
                factors.append(int(number / factor))
        factor += 1
    factors.sort()
    return factors


def is_number_prime(number):
    for divisor in range(2, math.ceil(math.sqrt(number))):
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
