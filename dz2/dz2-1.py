'''1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
 Элементы списка можно не запрашивать у пользователя, а указать явно, в программе'''

my_list = [3, 3.14, complex(7, 8), 'lol', [2, 5], (1, 2), {2, 8},
           frozenset([1, 2]), {'a': 19}, False,
           'ololo'.encode('utf8'), bytearray(b"some"), None]

for i in my_list:
    print(type(i))
