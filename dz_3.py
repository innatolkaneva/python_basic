# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
list_elem = [7, 9, 6, 5, 7, 8, 9]

def save_duplicate(list_elem):
    duplicate = []
    for elem in list_elem:
        if list_elem.count(elem) > 1:
            duplicate.append(elem)
    return list(set(duplicate))

def cut_duplicate(list_elem):
    list_elem = list(set(list_elem))
    return list_elem

if __name__ == '__main__':
    duplicate = save_duplicate(list_elem)
    print(duplicate)
    print(cut_duplicate(list_elem))
    
# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и
# регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
text = """Посадил дед репку — выросла репка большая-пребольшая. Стал дед репку из земли тащить: тянет-потянет, вытянуть не может.

Позвал дед на помощь бабку. Бабка за дедку, дедка за репку: тянут-потянут, вытянуть не могут.

Позвала бабка внучку. Внучка за бабку, бабка за дедку, дедка за репку: тянут-потянут, вытянуть не могут.

Кликнула внучка Жучку. Жучка за внучку, внучка за бабку, бабка за дедку, дедка за репку: тянут-потянут, вытянуть не могут.

Кликнула Жучка кошку Машку. Машка за Жучку, Жучка за внучку, внучка за бабку, бабка за дедку, дедка за репку: тянут-потянут, вытянуть не могут.

Кликнула кошка Машка мышку. Мышка за Машку, Машка за Жучку, Жучка за внучку, внучка за бабку, бабка за дедку, дедка за репку: тянут-потянут — вытащили репку!
"""
from pprint import pprint


def count_words(text):
    text_list = text.lower().split()
    text_dict = {}
    for word in text_list:
        if word.endswith(('.', ',', '!', ':')):
            word = word[:-1]
        text_dict.setdefault(word, 0)
        text_dict[word]+=1
    return text_dict

#больше 10 нет слов поэтому взяла 5
def most_frequent(text_dict):
    frequent_dict = {}
    for key, value in text_dict.items():
        if value >= 5:
            frequent_dict[key] = value
    return frequent_dict

dict_words = count_words(text)
pprint(most_frequent(dict_words))

'''Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.'''

items_bag = {
    'sleep_bag': 1,
    'tea': 0.1,
    'shugar': 0.5,
    'bootle_water': 1,
    'book': 0.7,
    't_short': 0.3,
    'trouses': 0.5,
    'laptop': 2,
    'sweetshot': 0.8,
    'bread': 0.9,
    'cup': 0.2,
    'table': 0.3
}

def pack_bag(massa, items_bag):
    camping_bag = []
    weight_bag = 0
    for item, weight in items_bag.items():
        weight_bag += weight
        if weight_bag <= massa:
            camping_bag.append(item)
        else:
            weight_bag -= weight
    return camping_bag

pprint(pack_bag(5, items_bag))

#Верните все возможные варианты комплектации рюкзака.
from itertools import combinations


def pack_all_bag(massa, items_bag):
    all_possible_packs = []
    for r in range(1, len(items_bag) + 1):
        for comb in combinations(items_bag.items(), r):
            total_weight = sum(item[1] for item in comb)
            if total_weight <= massa:
                all_possible_packs.append([item[0] for item in comb])
    return all_possible_packs

all_variant = pack_all_bag(3, items_bag)
print(f'Всего {len(all_variant)} вариантов')
for var in all_variant:
    pprint(var)