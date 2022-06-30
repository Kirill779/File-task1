file_name = 'Recipes.txt'

def file_rider(file_name,data, str) -> dict:
    coock_book = {}

    with open(file_name, mode, encoding='utf8') as file:
        if mode == 'r':
            for line in file:
                ingridient_recipe = line.strip()
                coock_book.setdefault(ingridient_recipe)
                position = file.readline()
                position_list = []
                for item in range(int(position)):
                    str_recipe = file.readline()
                    str_recipe = str_recipe.strip()
                    str_recipe = str_recipe.split('|')
                    ingridient_name = {}
                    ingridient_name.setdefault('ingredient_name', str_recipe[0])
                    ingridient_name.setdefault('quantity', str_recipe[1])
                    ingridient_name.setdefault('measure', str_recipe[2])
                    position_list.append(ingridient_name)
                file.readline()
                coock_book[ingridient_recipe] = position_list

        elif mode == 'w':
            with open('Coock_book.txt', 'w', encoding='utf8') as file:
                for i, k in coock_book.items():
                    file.write(str(i))
                    for ingredients in k:
                       file.write(str(ingredients) + '\n')

        else:
            pass

    return coock_book

def get_shop_list_by_dishes(dishes, person_count, kb):
    ingr_dish = {}
    num_dish = len(dishes)
    for dish in dishes:
        if dish in kb :
            if dish in ingr_dish:
                ingr_dish[dish]['quantity'] += (ingr_dish[dish]['quantity'])
            else:
                ingr_for_dish = {}
                ingr_for_dish['measure'] = kb[dish][0]['measure']
                ingr_for_dish['quantity'] = int(kb[dish][0]['quantity'])
            ingr_dish[dish] = ingr_for_dish
    for tel in ingr_dish.keys():
        print(tel)
        ingr_dish[tel]['quantity'] *= person_count

    print(ingr_dish)
    return


mode = 'r'
kb = file_rider(file_name, mode, str)
dishes = ['Запеченный картофель', 'Омлет', 'Омлет']
person_count = 3
get_shop_list_by_dishes(dishes, person_count,kb)