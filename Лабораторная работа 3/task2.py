# TODO Напишите функцию find_common_participants

def find_common_participants(first_group, second_group, separator=','):
    list_1 = first_group.split(separator)
    list_2 = second_group.split(separator)

    same_participants = set(list_1).intersection(set(list_2))
    participants_list = sorted(same_participants)  # Сортируем список
    return participants_list  # Возвращение отсортированного списка

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(common)  # Вывод списка общих участников
# TODO Провеьте работу функции с разделителем отличным от запятой
