# Треугольник существует только тогда,
# когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.
import math
import random


def quations():
    a = int(input('Введи сторону a'))
    b = int(input('Введи сторону b'))
    c = int(input('Введи сторону c'))
    return a, b, c


def is_exists(nums):
    if max(nums) > (sum(nums) - max(nums)):
        return False
    return True


def equilateral(nums):
    equal = 1
    for i in range(len(nums)):
        if nums[i - 1] == nums[i]:
            equal += 1
    if equal == 2:
        return 'Равнобедренный'
    elif equal > 2:
        return 'Равносторонний'
    return 'Не равнобедренный и не равносторонний'


def main():
    nums = quations()
    if is_exists(nums):
        print(equilateral(nums))
    else:
        print('Не существует')


main()

# 3. Напишите код, который запрашивает число и сообщает является ли оно простым
# или составным. Используйте правило для проверки:
# “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

MIN_NUM = 0
MAX_NUM = 100_000


def is_valid(num):
    if MIN_NUM < num < MAX_NUM:
        return True
    return False


def is_simple(num):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return 'Составное'
    else:
        return 'Простое'


def main2():
    answer = int(input('Введи число'))
    if is_valid(answer):
        print(is_simple(answer))
    else:
        print('Диапазон от 0 до 100000!')


main2()


# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число
# за 10 попыток. Программа должна подсказывать “больше” или “меньше” после
# каждой попытки.
def guess_the_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Программа загадала число от 0 до 1000. У вас есть 10 попыток, чтобы угадать его.")

    secret_number = random.randint(0, 1000)
    attempts = 10

    for attempt in range(attempts):
        try:
            guess = int(input(f"Попытка {attempt}. Введите ваше предположение: "))

            if guess < 0 or guess > 1000:
                print("Введите число в диапазоне от 0 до 1000.")
                continue

            if guess < secret_number:
                print("Загаданное число больше.")
            elif guess > secret_number:
                print("Загаданное число меньше.")
            else:
                print(f"Поздравляем! Вы угадали число {secret_number} за {attempt} попыток.")
                break
        except ValueError:
            print("Пожалуйста, введите число.")
    else:
        print(f"К сожалению, вы не угадали. Загаданное число было {secret_number}.")


guess_the_number()
