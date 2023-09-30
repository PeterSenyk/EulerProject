number_one = 998
number_two = 999

product = number_one * number_two
print(f"The product =", product)


def digit_list(entered_product):
    divisor = 10 ** (len(str(entered_product)) - 1 )
    print(f"The divisor =", divisor)
    digits = []
    while divisor > 0:
        new_digit = entered_product // divisor
        digits.append(new_digit)
        entered_product %= divisor
        divisor = divisor // 10
    return digits


pal_list = digit_list(product)

list_left = pal_list[:len(pal_list)//2]
print(list_left, f"= Left half of the list")
list_right = pal_list[len(pal_list)//2:]
list_right.reverse()
print(list_right, f"= Right half of the list reversed")

if list_left == list_right:
    print("true")
