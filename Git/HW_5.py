"""Спочатку напишіть код для читання та аналізу даних замовлення -
поділ замовлень по рядках та продуктів по «@@@».

Якщо завантажуємо файл у ручному форматі (зберегти файл через завантаження, то робимо ось так, головне щоб файл був в одній директорії з
кодом) Для того, щоб завантажити файл в автоматичному режимі ознайомтесь з пакетом requests

Потім напишіть код для розрахунку підтримки та впевненості для кожної пари продуктів.
1 - Список усіх продуктів
2 - Словник з кількістю кожного продукту
3 - Словник підрахунку кожної пари продуктів.(???)
4. Словник підрахунку пар містить підтримку кожної пари елементів.(???)
5. Використовуйте два словники, щоб розрахувати впевненість для кожної пари елементів.

* Зверніть увагу, що підтримка симетрична, а впевненість – ні.
Наприклад, якщо є 100 замовлень з "bananas", 200 замовлень з «peanut butter» та 30 замовлень з
обома, тоді впевненість bananas => peanut butter становить 30%, тоді як впевненість peanut butter => bananas - 15%.

* Пам'ятайте, що не можна розраховувати впевненість продукту в (вона завжди буде 100%, але це не цікаво).
Зрештою, враховуючи мінімальні вимоги до впевненості та підтримці, переберіть усі пари продуктів та надрукуйте пари,
що відповідають критеріям, у такому форматі:
Chunky Guacamole => Organic Tortilla Chips (5.37%)"""

def read_file(file: str):

    with open(file, mode='r') as file:
        data = file.read()
    return data

def read_and_processing_product_counts(data: str):

    orders = data.split('\n\n')
    product_list = {}
    for order in orders:
        products = order.split('@@@')
        for product in products:
            if product in product_list.keys():
                product_list[product] += 1
            else:
                product_list.update({product: 1})

    print("Product counts:", product_list)

def read_and_processing_unique_products(data: str):

    orders = data.split('\n\n')
    unique_products = set()

    for order in orders:
        products = order.split('@@@')
        for product in products:
            unique_products.add(product)
    print(f'Unique products:", {unique_products}')

all_combinations = []

def get_combinations(data: str):
    combinations = []

    for i in range(len(order)):
        for j in range(i, len(order)):
            combination = (order[i], order[j])
            combinations.append(combination)
    return set(combinations)


    for order in data:
        combinations = get_combinations(order)
        all_combinations.extend(combinations)

all_combinations_numbers = dict()

for item in all_combinations:
    if item in all_combinations_numbers.keys():
        all_combinations_numbers[item] += 1
    else:
        all_combinations_numbers.update({item: 1})


print(all_combinations_numbers)
unique_combinations = set(all_combinations)
print(unique_combinations)
count = len(unique_combinations)
print("Number of unique combinations:", count)

#########################################################################################################################

file = '/Users/mariashukaliuk/Downloads/orders123.txt'

data = read_file(file)

read_and_processing_product_counts(data)
# read_and_processing_unique_products(data)
# get_combinations(data)
find_combinations(data)
