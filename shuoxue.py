"""
轩氏数学计算库 XuanShuoxue
Copyright (c) 2023 轩哥啊哈OvO
"""
import math
import calendar


def add(a: float, b: float):
    return float(a + b)


def minus(a: float, b: float):
    return float(a - b)


def multiply(a: float, b: float):
    return float(a * b)


def divide(a: float, b: float):
    return float(a / b)


def power(a: float, b: float):
    return float(a ** b)


def root(a: float, b: float = 2):
    return float(a ** (1 / b))


def factorial(num: float):
    if (num > 1):
        result = num * factorial(num - 1)
    else:
        result = 1
    return result


def maximum_common_factor(a: float, b: float):
    if a > b:
        smaller = b
    else:
        smaller = a
    for num in range(1, smaller + 1):
        if (a % num == 0) and (b % num == 0):
            maximum_common_factor = num
    return maximum_common_factor


def minimum_common_multiple(a: float, b: float):
    if a > b:
        greater = a
    else:
        greater = a
    while (True):
        if (greater % a == 0) and (greater % b == 0):
            minimum_common_multiple = greater
            break
        greater += 1
    return minimum_common_multiple


def binary(num: int):
    return bin(num)[2:]


def octonary(num):
    return oct(num)[2:]


def hexadecimal(num):
    return hex(num)[2:].upper()


def sin(angle: float):
    return math.sin(math.radians(angle))


def cos(angle: float):
    return math.cos(math.radians(angle))


def tan(angle: float):
    return math.tan(math.radians(angle))


def is_prime(num: int):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def linear_equation_with_one_unknown(a: float, b: float):
    try:
        return b * (-1) / a
    except ZeroDivisionError:
        return False


def quadratic_equation_with_one_unknown(a: float, b: float, c: float):
    try:
        return [(b * -1 + math.sqrt(b ** 2 - 4 * a * c)) / (a * 2), (b * -1 - math.sqrt(b ** 2 - 4 * a * c)) / (a * 2)]
    except ValueError:
        return False


def multiplication_table(num: int):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print('{}x{}={}'.format(j, i, i * j), end=" ")
        print("")


def calendar_year_and_month(year: int, month: int):
    return calendar.month(year, month)

if __name__ == "__main__":
    multiplication_table(100)