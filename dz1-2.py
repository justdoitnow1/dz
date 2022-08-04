result = int(input('Введите время в секундах:'))
hour = result // 3600
min = (result - hour * 3600) // 60
with_min = hour * 3600 + min * 60

if result > with_min:
    sec = result - with_min
else:
    sec = 00

print(f'{result} это {hour}ч :{min}м :{sec}с')

