'''**Задание:**
1. Создайте список из 5 баг-репортов с разными приоритетами:
    - `"Ошибка 1 — High"`.
    - `"Ошибка 2 — Low"`.
    - И так далее.
2. Реализуйте следующие функции:
    - Добавление нового бага.
    - Удаление бага с низким приоритетом.
    - Сортировка багов по приоритету.'''

bugs = [
    {"name": "Ошибка 1", "priority": "High"},
    {"name": "Ошибка 2", "priority": "Low"},
    {"name": "Ошибка 3", "priority": "Critical"},
    {"name": "Ошибка 4", "priority": "Blocker"},
    {"name": "Ошибка 5", "priority": "Low"}
]

# Добавление нового бага.
def addNewBug(bugs, name, priority):
        newBug = {"name": name, "priority": priority}
        bugs.append(newBug)
addNewBug(bugs, "Ошибка 6", "Blocker")
print(bugs)

# Сортировка багов по приоритету.
priority_order = {"Blocker": 0, "Critical": 1, "High": 2, "Low": 3}
sorted_bugs = sorted(bugs, key=lambda x: priority_order[x["priority"]])
print(sorted_bugs)

# Удаление бага с низким приоритетом.
filtered_bugs = []

for bug in bugs:
    if bug["priority"] != "Low":
        filtered_bugs.append(bug)
print(filtered_bugs)


