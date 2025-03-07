# **Задание:**
# 1. Создайте словарь с информацией о баге:
#     - ID.
#     - Название.
#     - Статус.
# 2. Измените статус баг-репорта.
# 3. Напишите текстовое объяснение о неизменяемых типах данных
# (например, `str`, `int`, `tuple`) в отдельном файле `data_types.txt`.

bug = {"ID": "1", "Название": "Баг 1", "Статус": "в работе"}

print(id(bug))  # Выводит 1922247874560

print(bug)

bug["Статус"] = "новый_статус"

print(id(bug)) # Выводит 1922247874560

print(bug) # Выводит тот же id, но статус мы видим изменённый
