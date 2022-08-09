result = int(input('Введите время в секундах:'))
hour = result // 3600
min = (result - hour * 3600) // 60
with_min = hour * 3600 + min * 60
sec = result - with_min
print(f'{result} секунд это {hour:02}ч :{min:02}м :{sec:02}с')

