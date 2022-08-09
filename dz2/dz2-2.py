"""2. Для списка реализовать обмен значений соседних элементов.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
При нечётном количестве элементов последний сохранить на своём месте.
Для заполнения списка элементов нужно использовать функцию input()."""

a = list(input('Введите цифры для списка, через запятую:').split(','))

if len(a) % 2 != 0:
    last = a.pop()
else:
    last = False

slice_a = a[::2]
slice_b = a[::-2]
slice_b.reverse()
a.clear()

for i in range(len(slice_a)):
    a.append(slice_b[i])
    a.append(slice_a[i])

if last is True:
    a.append(last)

print(a)