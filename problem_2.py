number_one = 1
number_two = 2
fib_number = number_two
sum = 0

while fib_number <= 4000000:
    if fib_number % 2 == 0:
        sum += fib_number

    fib_number += number_one
    number_one = number_two
    number_two = fib_number

print(sum)
