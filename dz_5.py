# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
import os
from pprint import pprint


def info_about_file(path: str) -> tuple[str, str, str]:
    path_to_file = os.path.dirname(path)
    file_name = os.path.basename(path)
    extend = os.path.splitext(file_name)[1]
    return path_to_file, file_name, extend

file = os.path.join(os.getcwd(), 'dz_5.py')
print(info_about_file(file))

#Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии

def generation_dict(names: list[str], procent: list[str], wage: list[int]) -> dict:
    bonus_dict = {name: wage * (float(procent[:-1])/100) for name, procent, wage in zip(names, procent, wage)}
    return bonus_dict
names = ['Inna', 'Ira', 'Boris']
procent = ['10.50%', '20.00%', '13.00%']
wage = [28_000, 31_000, 41_000]
pprint(generation_dict(names, procent, wage))

# Создайте функцию генератор чисел Фибоначчи
def nums_fibonacci(n: int) -> list[int]:
    if n < 0:
        raise ValueError('n must be greater than 0')
    elif n in [0, 1, 2]:
        yield 0
        yield 1
        yield 1
    else:
        list_fibonacci = [0, 1]
        for i in range(n-2):
            list_fibonacci.append(list_fibonacci[-1] + list_fibonacci[-2])
        for num in list_fibonacci:
            yield num
for i in nums_fibonacci(10):
    print(i)

