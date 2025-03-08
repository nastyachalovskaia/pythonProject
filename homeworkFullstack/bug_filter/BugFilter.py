# **Задание:**
# Напишите программу, которая:
# 1. Создает список из 7 баг-репортов (пример: `"Ошибка 1 – High"`, `"Ошибка 2 – Medium"`).
# 2. Запрашивает у пользователя приоритет (`High`, `Medium` или `Low`).
# 3. Выводит только баги с указанным приоритетом.
# 4. Если таких багов нет, программа сообщает об этом.

bugs = [
    "Ошибка 1 – High",
    "Ошибка 2 – Medium",
    "Ошибка 3 – Low",
    "Ошибка 4 – High",
    "Ошибка 5 – High",
    "Ошибка 6 – Medium",
    "Ошибка 7 – Low"
]

choose_priority = input("Введите приоритет для поиска (High, Medium, Low): ").strip().capitalize()

filtered_bugs = [bug for bug in bugs if bug.endswith(choose_priority)]

if filtered_bugs:
    print(f"Найденные баги:")
    for bug in filtered_bugs:
        print(f" - {bug}")
else:
    print(f"Баг-репортов с приоритетом {choose_priority} нет.")
