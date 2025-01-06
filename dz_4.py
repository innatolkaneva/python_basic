#Напишите функцию для транспонирования матрицы
import decimal
from pprint import pprint
from typing import List

matr = [
    [1, 3, 3],
    [1, 2, 7],
    [4, 5, 6],
    [2, 3, 1]
]


def transpon(matr1: List):
    matr2 = []
    for i in range(len(matr1[0])):
        new_row = []
        for r in matr1:
            new_row.append(r[i])
        matr2.append(new_row)
    return matr2


pprint(transpon(matr))


# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.
def infinity(**kwargs):
    new_dict = {}
    for key, val in kwargs.items():
        try:
            if hash(key):
                new_dict[val] = key
        except TypeError:
            new_dict[str(val)] = key
    return new_dict


pprint(infinity(
    a=[1, 2, 3],
    b=8,
    c={9, 3}
))
#Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.

from decimal import Decimal

MIN_SUM = 50
PROCENT_COMMISION = 0.015
MIN_COMMISION = 30
MAX_COMMISION = 600
BONUS = 0.03
LIMIT_BEFORE_TAX = 5_000_000
TAX_RATE = 0.1

list_operation = []


def menu(balance: Decimal, count: int, run: bool):
    print('Добро пожаловать!')
    dict_menu = {
        'comand': 'Выберите команду',
        '1': 'Пополнить счет',
        '2': 'Снять со счета',
        '3': 'Отобразить операции',
        '0': 'Выйти',
    }
    for k, v in dict_menu.items():
        if k.isdigit():
            print(f'{k}: {v}')
        else:
            print(v)
    if balance > LIMIT_BEFORE_TAX:
        balance *= (1 - TAX_RATE)
    choice = input('введи команду')
    if choice == '1':
        balance = give_money(balance, list_operation)
        count += 1
    elif choice == '2':
        balance = get_money(balance, list_operation)
        count += 1
    elif choice == '3':
        print_operation()
    elif choice == '0':
        run = False

    else:
        print('Нет такой команды')
    if count %3 == 0:
        balance *= (1 + BONUS)
    print("Это ваш баланс ", balance)
    return balance, run


def give_money(balance: Decimal, list_operation: List):
    try:
        money_to_give = Decimal(input('Введите сумму пополнения'))
        if money_to_give % MIN_SUM == 0:
            final_balance = balance + money_to_give
            list_operation.append(f'Выдача денег, начальный баланс {balance}, сумма {money_to_give}, конечный {final_balance}')
            return final_balance
        else:
            print(f'Сумма не кратна {MIN_SUM}')
            return balance
    except decimal.InvalidOperation:
        print("Это не число")
        give_money(balance)


def get_money(balance: Decimal, list_operation: List):
    try:
        money_to_get = Decimal(input('Введите сумму снятия'))
        procent = money_to_get * Decimal(PROCENT_COMMISION)
        if money_to_get % MIN_SUM == 0:
            if procent < MIN_COMMISION:
                procent = MIN_COMMISION
            elif procent > MAX_COMMISION:
                procent = MAX_COMMISION
        else:
            print(f'Сумма не кратна {MIN_SUM}')
            return balance
        if money_to_get + procent <= balance:
            final_balance = balance - (money_to_get + procent)
            list_operation.append(f'Выдача денег, начальный баланс {balance}, сумма {money_to_get}, конечный {final_balance}')
            return final_balance
        return balance

    except decimal.InvalidOperation:
        print("Это не число")
        get_money(balance)


def print_operation():
    pprint(list_operation)

if __name__ == '__main__':
    print('Добро пожаловать!')
    balance = Decimal(0)
    count = 1
    run = True
    while run:
        balance, run = menu(balance, count, run)