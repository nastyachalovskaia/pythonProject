'''**Задание:**
Напишите программу, которая:
1. Запрашивает у пользователя количество тест-кейсов, выполненных за каждый день недели.
2. Выводит:
    - Общее количество тестов за неделю.
    - Среднее количество тестов в день.
3. Выводит сообщение в зависимости от результата:
    - Если среднее больше 10: `"Отличная работа!"`.
    - Иначе: `"Попробуйте улучшить результат."`.'''

all_tests_per_seven_days = {}

days_of_week = ["Понедельник ", "Вторник ", "Среда ", "Четверг ", "Пятница ", "Суббота ", "Воскресенье "]

for day in days_of_week:
    tests = input(f"Введите количество тестов в {day}")
    all_tests_per_seven_days[day] = int(tests)

general_number_of_tests_per_week = sum(all_tests_per_seven_days.values())
print(f"Вы сделали {general_number_of_tests_per_week} тестов за неделю")

average_number_of_tests_per_day = general_number_of_tests_per_week / len(all_tests_per_seven_days)

if average_number_of_tests_per_day >= 10:
    print("Отличная работа!")
else:
    print("Попробуйте улучшить результат.")
