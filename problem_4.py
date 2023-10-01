"""Largest palindrome product of two 3-digit numbers"""


def digit_list(entered_product):
    divisor = 10 ** (len(str(entered_product)) - 1)
    digits = []
    while divisor > 0:
        new_digit = entered_product // divisor
        digits.append(new_digit)
        entered_product %= divisor
        divisor = divisor // 10
    return digits


def list_split(entered_list):
    half_list = len(entered_list) // 2

    return entered_list[:half_list], entered_list[half_list:]


def palindrome_check(one, two):
    if one == two:
        return True
    else:
        return False


number_one = 99
number_two = 99

for x in range(100, 1):
    print(x)


for x in range(1000, 1):
    for y in range(1000, 99):
        product_num = number_one * number_two
        dig_list = digit_list(number_one * number_two)
        left, right = list(list_split(dig_list))
        right.reverse()
        if palindrome_check(left, right):
            print(number_one, number_two, (number_one * number_two))
            break
        else:
            number_one -= 1
number_two -= 1
