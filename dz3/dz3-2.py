"""2. Выполнить функцию, которая принимает несколько параметров,
 описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
 Функция должна принимать параметры как именованные аргументы.
  Осуществить вывод данных о пользователе одной строкой."""

name = input('Введите имя пользователя:')
surname = input('Введите фамилию пользователя:')
year = input('Введите год рождения:')
city = input('Введите город проживания:')
email = input('Введите email:')
tel = input('Введите телефон:')


def foo_str(**kwargs):
    return f"Имя {kwargs['name']} Фамилия {kwargs['surname']} Год рождения {kwargs['year']}" \
           f" Город {kwargs['city']} email {kwargs['email']} Телефон {kwargs['tel']}"


print(foo_str(name=name, surname=surname, year=year, city=city, email=email, tel=tel))
