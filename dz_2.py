# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
import math


def _hex(num):
    right = num
    hex_num = ''
    while num > 0:
        remains = num % 16
        if remains > 9:
            chars = 'abcdef'
            remains = chars[remains - 10]
        hex_num += str(remains)
        num //= 16
    hex_num = hex_num[::-1]
    if hex_num == hex(right)[2:]:
        return hex_num
    return False


def main():
    answer = int(input('Введи число'))
    print(_hex(answer))


main()
# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions
import fractions


def list_num(num1: str, num2: str):
    num1 = num1.split('/')
    num2 = num2.split('/')
    return num1, num2


def simplify_fraction(numerator: int, denominator: int):
    gcd = math.gcd(numerator, denominator)
    return numerator // gcd, denominator // gcd


def sum_num(nums: tuple, num1, num2):
    a, b = nums
    if a[1] != b[1]:
        a = [int(num) for num in a]
        b = [int(num) for num in b]
        divider1 = a[1]
        divider2 = b[1]
        a = [num * divider2 for num in a]
        b = [num * divider1 for num in b]
    sum_ = [a[0] + b[0], a[1]]
    sum_ = simplify_fraction(*sum_)
    sum_ = [str(val) for val in sum_]
    if str(fractions.Fraction(num1) + fractions.Fraction(num2)) == '/'.join(sum_):
        return '/'.join(sum_)


def mult_num(nums: tuple, num1: str, num2: str):
    a, b = nums
    mult = [int(num1) * int(num2) for num1, num2 in zip(a, b)]
    mult = simplify_fraction(*mult)
    mult = [str(val) for val in mult]
    if str(fractions.Fraction(num1) * fractions.Fraction(num2)) == '/'.join(mult):
        return '/'.join(mult)


def main2():
    answer = input('Введи дробь через /')
    answer2 = input('Введи 2 дробь через /')
    nums = list_num(answer, answer2)
    print(sum_num(nums, answer, answer2))
    print(mult_num(nums, answer, answer2))


main2()
