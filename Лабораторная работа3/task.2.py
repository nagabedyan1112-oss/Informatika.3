def find_common_participants(group1: str, group2: str, delimiter: str = ","):
    # Разделяем строки и убираем лишние пробелы
    participants1 = [p.strip() for p in group1.split(delimiter) if p.strip()]
    participants2 = [p.strip() for p in group2.split(delimiter) if p.strip()]
    # Находим общих участников
    common = set(participants1) & set(participants2)
    # Возвращаем отсортированный список
    return sorted(common)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_list = find_common_participants(
    participants_first_group,
    participants_second_group,
    delimiter="|"
)

print(common_list)