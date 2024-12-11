# TODO Напишите функцию для поиска индекса товара
def find_item_in_list(items_list, item):
    for i in range(len(items_list)):
        if items_list[i] == item:
            return i  # Возвращаем индекс первого вхождения
    return None  # Если элемент не найден


items_list2 = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
item2 = ['банан', 'груша', 'персик']

for find_item in item2:
    index_item = find_item_in_list(items_list2, find_item)  # Передаем текущий элемент
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
