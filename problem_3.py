import math

# initial_number = 600861475143
initial_number = 20
factor = 1
prime = 1
factor_list = list()
prime_list = [2]


while factor <= initial_number:
    if initial_number % factor == 0:
        factor_list.append(factor)
    factor += 1

print(factor_list)
factor_list.reverse()
print(factor_list)
position_zero = 0
possible_factor = 2

