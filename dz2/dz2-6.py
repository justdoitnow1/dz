count = 0
product_list = []
product_dict = {}
while True:
    count += 1
    name = input('Введите название товара: ')
    price = float(input('Введите цену товара: '))
    total = float(input('Введите количество товара: '))
    value = input("Введите единицу измерения товара: ")
    product_tpl = (count, {"Название товара": name,
                           "Цена": price, "Количество": total,
                           "ед": value})

    product_list.append(product_tpl)

    if input('Вы закончили? (y/n)') == 'y':
        break

for v in product_list:
    for product, val in v[1].items():
        if v[0] == 1:
            product_dict[product] = []
        product_dict[product].append(val)

print(product_dict)
