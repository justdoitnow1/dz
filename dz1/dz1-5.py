print('Введите прибыль и издержки вашей фирмы')
total = int(input('Введите выручку:'))
loss = int(input('Введите издержки:'))
if total > loss:
    profit = total-loss
    print(f'Фирма в прибыли, выручка больше издержек на {profit}')
    # Рентабельность продаж по валовой прибыли = Валовая прибыль / Выручка
    print(f'Рентабельность {profit / total}')
    peoples = int(input('Сколько у вас сотрудников?'))
    print(f'Фирма зарабатывает {total / peoples} на каждого сотрудника')
elif total == loss:
    print(f'Убытки равны прибыли')
else:
    print(f'Фирма в убытке, издержки больше выручки на {loss - total}')

