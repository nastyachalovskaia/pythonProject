# **Задание:**
# 1. Запросите у пользователя строку **с ошибкой** из лога (`"Ошибка: тест не пройден из-за ошибки в модуле auth"`)
# 2. Преобразуйте ее, удалив лишние пробелы и заменив `"Ошибка"` на `"Ошибка критическая"`
# 3. Разбейте строку на слова и выведите список.

stroka = "Ошибка: тест не пройден из-за ошибки в модуле auth"

original_string = str(input("Введите строку лога "))

if "Ошибка" in original_string:
    print("В логе есть инфо об ошибке")
else:
    print("Попробуйте ещё раз")

changed_string_with_no_trims = original_string.strip().replace('Ошибка', 'Ошибка критическая')

print(f"Обработанная строка: {changed_string_with_no_trims}")

words = changed_string_with_no_trims.split()

print(f"Разбитый текст: {words}")
