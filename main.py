from pprint import pprint


def cook_book_maker():  # При вызове считывает данные из файла и формирует книгу рецептов
    with open('cookbook.txt', 'r') as book:

        cook_book = {}

        while True:
            dish_name = book.readline().strip(' \n')
            if dish_name == '':
                break
            ingredients_count = int(book.readline())

            ingredients_list = []
            for i in range(ingredients_count):
                line = book.readline().split('|')
                ingredients_list.append(
                    {'ingredient_name': line[0].strip(), 'quantity': int(line[1]), 'measure': line[2].strip(' \n')})
            cook_book[dish_name] = ingredients_list

            book.readline()

    return cook_book


# Задача №2
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = cook_book_maker()
    ingredients = {}

    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredients.get(ingredient['ingredient_name']) == None:
                ingredients[ingredient['ingredient_name']] = {
                    'measure': '?', 'quantity': 0}

            ingredients[ingredient['ingredient_name']
                        ]['quantity'] += person_count * ingredient['quantity']
            ingredients[ingredient['ingredient_name']
                        ]['measure'] = ingredient['measure']

    return ingredients


# Задача №3
def file_uniter(filenames_list):  # Результат выполнения функции записывается в файл result.txt
    files = []

    for filename in filenames_list:
        with open(filename, 'r') as file:

            content = file.read()
            strcount = content.count('\n') + 1
            files.append({
                'name': filename,
                'strcount': strcount,
                'content': content
            })

    files = sorted(files, key=lambda file: file['strcount'])
    with open('result.txt', 'w') as result:
        for file in files:
            result.write(file['name'] + '\n')
            result.write(str(file['strcount']) + '\n')
            result.write(file['content'] + '\n')


if __name__ == '__main__':
    print("Первое Задание:\n")
    pprint(cook_book_maker())
    print()
    print("Второе Задание:\n")
    pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
    print()
    file_uniter(["1.txt", "2.txt", "3.txt"])

