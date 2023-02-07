"""
基于Java的Python数学计算库 JPyMath

Copyright (c) 2023 轩哥啊哈OvO

"""
import jpype
jpyJVM = jpype.startJVM(jpype.getDefaultJVMPath())
_jpymath = jpype.JClass('jpymath')

def add(x: float, y: float):
    return _jpymath.add(x, y)

def minus(x: float, y: float):
    return _jpymath.minus(x, y)

def multiply(x: float, y: float):
    return _jpymath.multiply(x, y)

def divide(x: float, y: float):
    return _jpymath.divide(x, y)

def power(x: float, y: float):
    return _jpymath.power(x, y)

def root(x: float, y: float):
    return _jpymath.root(x, y)

def bigger(x: float, y: float):
    return _jpymath.bigger(x, y)

def smaller(x: float, y: float):
    return _jpymath.smaller(x, y)

def isEqual(x: float, y: float):
    return _jpymath.isEqual(x, y)

def factorial(num: int):
    return _jpymath.factorial(num)

def maximum_common_factor(a: int, b: int):
    return _jpymath.maximum_common_factor(a, b)

def minimum_common_multiple(a: int, b: int):
    return _jpymath.minimum_common_multiple(a, b)

def sin(angle: float):
    return _jpymath.sin(angle)

if __name__ == '__main__':
    print(sin(30))

# def binary(num: int):
#     return bin(num)[2:]

# def octonary(num):
#     return oct(num)[2:]

# def hexadecimal(num):
#     return hex(num)[2:].upper()

# def sin(angle: float):
#     return math.sin(math.radians(angle))

# def cos(angle: float):
#     return math.cos(math.radians(angle))

# def tan(angle: float):
#     return math.tan(math.radians(angle))

# def is_prime(num: int):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def linear_equation_with_one_unknown(a: float, b: float):
#     try:
#         return b * (-1) / a
#     except ZeroDivisionError:
#         return False

# def quadratic_equation_with_one_unknown(a: float, b: float, c: float):
#     try:
#         return [(b * -1 + math.sqrt(b ** 2 - 4 * a * c)) / (a * 2), (b * -1 - math.sqrt(b ** 2 - 4 * a * c)) / (a * 2)]
#     except ValueError:
#         return False

# def multiplication_table(num: int):
#     for i in range(1, num + 1):
#         for j in range(1, i + 1):
#             print('{}x{}={}'.format(j, i, i * j), end=" ")
#         print("")

# def calendar_year_and_month(year: int, month: int):
#     return calendar.month(year, month)


# if __name__ == "__main__":
#     multiplication_table(100)