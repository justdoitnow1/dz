"""2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
 Для его формирования используйте генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]."""

s_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

a = [n for i, n in enumerate(s_list) if n > s_list[i-1] and n != s_list[0]]
print(a)
