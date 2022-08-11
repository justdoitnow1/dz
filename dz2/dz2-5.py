"""5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
 У пользователя нужно запрашивать новый элемент рейтинга.
 Если в рейтинге существуют элементы с одинаковыми значениями,
 то новый элемент с тем же значением должен разместиться после них."""

rating_list = [7, 5, 3, 3, 2]
print(f'Ваш рейтинг: {rating_list}')

while True:

    user_digit = int(input('Введите цифру рейтинга, для выхода введите 0:'))
    if user_digit == 0:
        break
    rating_count = rating_list.count(user_digit)
    if rating_list.count(user_digit):
        if rating_count == 1:
            rating_list.insert(rating_list.index(user_digit) + 1, user_digit)
        else:
            rating_list.insert(rating_list.index(user_digit) + rating_count, user_digit)
    elif rating_list[-1] >= user_digit:
        rating_list.append(user_digit)
    elif rating_list[0] <= user_digit:
        rating_list.insert(0, user_digit)

    print(rating_list)
