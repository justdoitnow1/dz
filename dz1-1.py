print('Вас приветствует простой калькулятор, пожалуйста введите два числа и знак действия')
num1 = int(input('Введите первое число'))
print('Теперь введите второе число')
num2 = int(input('Введите второе число'))
print('Введите желаемый знак ("+" "-" "*" "/")')
sign = input('Введите знак')

if sign == '+':
    result = num1 + num2
elif sign == '-':
    result = num1 - num2
elif sign == '*':
    result = num1 * num2
elif sign == '/':
    result = num1 / num2
else:
    result = 'Отсутствует, введен некорректный знак действия'

print('Ваш результат:', result)