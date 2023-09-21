##initial_number = 600861475143
import math
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

def check_prime(number_to_check):
    while possible_factor <= sqrt(factor_list[position_zero])
    possible_factor = 2
    if number_to_check % possible_factor == 0


# while prime < initial_number:
#     if prime % prime_list.range(0, prime_list+1) != 0:
#         prime_list.append(prime)
#     prime += 1

# def check_prime (prime):
#     for prime_list in factor_list:
#         if prime % prime_list != 0:
#             prime_list.append(prime)
#         prime += 1
#     return prime_list
#
# def check_prime_factor (factor_list):
#     factor_list.sort(reverse = True)
#     for prime_check in prime_list:
#         if factor_list[0] % prime_list == 0:
#             print(factor_list[0])








