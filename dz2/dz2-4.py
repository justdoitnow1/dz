"""4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове."""

input_result = input('Введите строку из нескольких слов разделенных пробелами:').split()
input_result = ' '.join(input_result)
output = ' '
i = 0
count = 0

while i < len(input_result):
    if input_result[i] == ' ' or i == len(input_result) - 1 and len(input_result) > 1:
        output = str(input_result[:i + 1])
        input_result = input_result[len(output):]
        i = i - len(output) + 1
        count += 1
        print(f'Cтрока {count}: {output}') if len(output) < 10 else print(f'Cтрока {count}: {output[: 11]}')
    i += 1

#Можно в несколько строчек, но очень уж хотелось поэксперементировать со строками
input_result = input('Введите строку из нескольких слов разделенных пробелами:').split()
a = 0
for i in input_result:
    a += 1
    print(f'Cтрока {a}: {i}')

