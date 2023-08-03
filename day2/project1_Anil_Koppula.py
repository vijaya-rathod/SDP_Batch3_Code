is_even = lambda num: int(num) & 1 == 0
is_odd = lambda num: not is_even(num)

def get_sum(num):
    _sum = 0
    for n in str(num):
        _sum += int(n)
    if len(str(num)) > 1:
        return get_sum(_sum)
    return _sum

def is_divisible_by_2(number):
    return str(number)[-1] in {'0', '2', '4', '6', '8'}

def is_divisible_by_3(number):
    # return sum(int(digit) for digit in str(number)) in {3, 6, 9}
    return get_sum(number) in {0, 3, 6, 9}

# def is_divisible_by_4(number):
#     last_two_digits = int(str(number)[-2:])
#     return last_two_digits in {0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96}
def is_divisible_by_4(number):
    if len(str(number)) == 1:
        return number in (4, 8) 
    else: 
        return str(number)[-1] in ('0', '4', '8') if is_even(str(number)[-2]) else str(number)[-1] in ('2', '6')

def is_divisible_by_5(number):
    return str(number)[-1] in {'0', '5'}

def is_divisible_by_6(number):
    return is_divisible_by_2(number) and is_divisible_by_3(number)


def is_divisible_by_7(number):
    str_number = str(number)
    if len(str_number.strip('-')) == 2:
        return number in {0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98}
    else:
        while len(str_number) != 2:
            last_digit = str_number[-1]
            except_last_digit = str_number[:-1]
            str_number = str(int(except_last_digit) - (9 * int(last_digit)))
        return int(str_number.strip('-')) in {0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98}

def is_divisible_by_8(number):
    eight_multiples = {0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96}
    if len(str(number)) == 1:
        return number == 8
    elif len(str(number)) == 2:
        return number in eight_multiples
    else:
        str_number = str(number)
        hundreds_digit = str_number[-3]
        if is_even(hundreds_digit):
            return int(str_number[-2:]) in eight_multiples
        else:
            return int(str_number[-2:])+4 in eight_multiples

# def is_divisible_by_9(number):
#     return sum(int(digit) for digit in str(number)) in {0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90}
def is_divisible_by_9(number):
    return get_sum(number) in {0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90}



number = 105
print(f"Is {number} divisible by 7? {is_divisible_by_7(number)}")
