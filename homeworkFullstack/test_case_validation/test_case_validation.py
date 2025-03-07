# **Задание:**
# Напишите программу, которая:
# 1. Запрашивает у пользователя количество тест-кейсов, которые он выполнил за день.
# 2. Проверяет, что введенное значение – это положительное целое число.
# 3. Если ввод некорректный (отрицательное число, строка, пустой ввод), программа просит ввести данные снова.
# 4. После корректного ввода программа выводит сообщение:
#     - `"Отличная работа!"`, если число тест-кейсов больше 10.
#     - `"Попробуйте улучшить результат."`, если меньше или равно 10.

allTestsPerSevenDays = {}

daysOfWeek = ["Понедельник ", "Вторник ", "Среда ", "Четверг ", "Пятница ", "Суббота ", "Воскресенье "]

for day in daysOfWeek:
    while True:
        userInput = input(f"Введите количество тестов в {day}").strip()
        if not userInput:
            print("Вы ввели пустую строку. Повторите ввод.")
            continue
        tests = int(userInput)
        if tests >= 0:
            allTestsPerSevenDays[day] = int(tests)
            break
        else:
            print("Пожалуйста, повторите ввод. Количество кейсов должно быть положительным целым числом")


generalNumberOfTestsPerWeek = sum(allTestsPerSevenDays.values())
print(f"Вы сделали {generalNumberOfTestsPerWeek} тестов за неделю")

averageNumberOfTestsPerDay = generalNumberOfTestsPerWeek/len(allTestsPerSevenDays)

if averageNumberOfTestsPerDay >= 10:
    print("Отличная работа!")
else:
    print("Попробуйте улучшить результат.")