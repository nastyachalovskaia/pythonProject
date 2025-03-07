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

choosePriority = input("Введите приоритет для поиска (High, Medium, Low): ").strip().capitalize()

filteredBugs = [bug for bug in bugs if bug.endswith(choosePriority)]

#  Функция enumerate() принимает список и возвращает индекс и значение каждого элемента в формате объекта.
#  Этот объект можно использовать в цикле for для обхода списка.
indices = [i for i, bug in enumerate(bugs) if bug.endswith(choosePriority)]

if filteredBugs:
    print(f"Найденные баги:")
    for bug in filteredBugs:
        print(f" - {bug}")
else:
    print(f"Баг-репортов с приоритетом {choosePriority} нет.")


