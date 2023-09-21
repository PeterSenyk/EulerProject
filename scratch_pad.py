initial_number = 678888
factor = 1
prime = 2
factor_list = []
prime_list = []

while factor < initial_number:
    if initial_number % factor == 0:
        factor_list.append(factor)
    factor += 1
    factor_list.sort(reverse=True)

while prime < factor_list[0]:
    if prime % factor_list[0] != 0:
        prime_list.append(prime)
    factor_list.pop(0)
    prime += 1

print(prime_list)
