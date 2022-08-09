"""3. Пользователь вводит месяц в виде целого числа от 1 до 12.
 Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
 Напишите решения через list и dict."""


while True:
    input_result = int(input("Введите номер месяца в виде целого числа от 1 до 12:"))

    if input_result > 12 or input_result == 0:
        print("Введите корректный номер месяца")
    else:
        break

month_dict = {"Зима": [12, 1, 2], "Весна": [3, 4, 5],
              "Лето": [6, 7, 8], "Осень": [9, 10, 11]}

for k, v in month_dict.items():
    if input_result in v:
        print(k)