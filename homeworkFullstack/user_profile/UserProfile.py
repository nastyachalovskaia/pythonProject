'''**Задание:**
1. Создайте переменные для хранения информации:
    - Имя пользователя.
    - Профессия.
    - Любимый инструмент для тестирования.
2. Позвольте пользователю изменить данные через ввод.
3. Добавьте проверку: если пользователь не ввел данные, программа выводит сообщение об ошибке.'''

def check_data():

    profile = {}

    while True:

        usr_name = input("Введите имя: ")

        if usr_name.strip():
            profile["Имя пользователя"] = usr_name
            print(f"Вы ввели: {usr_name}")
            break
        else:
            print("Вы ввели пустые данные об имени. Попробуйте еще раз.")

    while True:
        profession = input("Введите профессию: ")

        if profession.strip():
            profile["Профессия"] = profession
            print(f"Вы ввели: {profession}")
            break
        else:
            print("Вы ввели пустые данные о профессии. Попробуйте еще раз.")

    while True:
        favorite_test_tool = input("Введите любимый инструмент для тестирования: ")

        if favorite_test_tool.strip():
            profile["Любимый инструмент для тестирования"] = favorite_test_tool
            print(f"Вы ввели: {favorite_test_tool}")
            break
        else:
            print("Вы ввели пустые данные о любимом инструменте для тестирования. Попробуйте еще раз.")
    return profile


original_profile = check_data()

change_data = input("Хотите изменить данные? Если да, то введите да или ok. Если нет, нажмите Enter: ")

if change_data.strip().lower() == "да" or "ok":
    new_profile = check_data()
    original_profile.update(new_profile)
    print("Данные изменены")
else:
    print("Изменения завершены")

print(f"Итоговые данные: {original_profile}")
