"""4. Программа принимает действительное положительное число x и целое отрицательное число y.
 Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
  При решении задания нужно обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
 Первый — возведение в степень с помощью оператора **.
  Второй — более сложная реализация без оператора **, предусматривающая использование цикла."""

while True:
    try:
        a = float(input('Введите действительное положительное число:'))
        b = int(input('Введите целое отрицательное число:'))
        if b >= 0 or a <= 0:
            int('err')

    except ValueError:
        print('Ошибка при вводе чисел, пробуем еще раз')
        continue
    break


def func_with(x=a, y=b):
    return x ** y


def my_func(x=a, y=b):
    p = x
    for i in range(abs(y)-1):
        x = x * p
    x = 1 / x
    return x


print(func_with())
print(my_func())