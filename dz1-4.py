result = int(input('Введите целое, положительное число:'))
num = result
max = 0
while num // 10 > 0:
    empnum = num % 10 #Отделили последнюю цифру
    if max < empnum:
        max = empnum
    num //= 10  #Уменьшили на последнюю цифру
print('Максимальное число из %i это %i' % (result, max))




