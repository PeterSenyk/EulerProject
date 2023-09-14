number_one = 1
number_two = 2
fib_number = 0
sum = 0

while fib_number <= 4000000:
    if fib_number % 2 == 0:
        sum += fib_number

    fib_number = number_one
    print("fib", fib_number)
    number_two += number_one
    print("two", number_two)
    number_one += fib_number
    print("one", number_one)


print(sum)
