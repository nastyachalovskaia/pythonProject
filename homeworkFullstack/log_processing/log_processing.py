# **Задание:**
# 1. Запросите у пользователя строку **с ошибкой** из лога (`"Ошибка: тест не пройден из-за ошибки в модуле auth"`)
# 2. Преобразуйте ее, удалив лишние пробелы и заменив `"Ошибка"` на `"Ошибка критическая"`
# 3. Разбейте строку на слова и выведите список.

stroka = "Ошибка: тест не пройден из-за ошибки в модуле auth"

originalString = str(input("Введите строку лога "))

if "Ошибка" in originalString:
    print("В логе есть инфо об ошибке")
else:
    print("Попробуйте ещё раз")

changedStringWithNoTrims = originalString.replace('Ошибка', 'Ошибка критическая').strip()

print(f"Обработанная строка: {changedStringWithNoTrims}")

words = changedStringWithNoTrims.split()
print(f"Разбитый текст: {words}")