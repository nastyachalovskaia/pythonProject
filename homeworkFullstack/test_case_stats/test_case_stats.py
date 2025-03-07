'''**Задание:**
Напишите программу, которая:
1. Запрашивает у пользователя количество тест-кейсов, выполненных за каждый день недели.
2. Выводит:
    - Общее количество тестов за неделю.
    - Среднее количество тестов в день.
3. Выводит сообщение в зависимости от результата:
    - Если среднее больше 10: `"Отличная работа!"`.
    - Иначе: `"Попробуйте улучшить результат."`.'''

allTestsPerSevenDays = {}

daysOfWeek = ["Понедельник ", "Вторник ", "Среда ", "Четверг ", "Пятница ", "Суббота ", "Воскресенье "]

for day in daysOfWeek:
    tests = input(f"Введите количество тестов в {day}")
    allTestsPerSevenDays[day] = int(tests)

generalNumberOfTestsPerWeek = sum(allTestsPerSevenDays.values())
print(f"Вы сделали {generalNumberOfTestsPerWeek} тестов за неделю")

averageNumberOfTestsPerDay = generalNumberOfTestsPerWeek/len(allTestsPerSevenDays)

if averageNumberOfTestsPerDay >= 10:
    print("Отличная работа!")
else:
    print("Попробуйте улучшить результат.")