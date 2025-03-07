'''**Задание:**
1. Создайте переменные для хранения информации:
    - Имя пользователя.
    - Профессия.
    - Любимый инструмент для тестирования.
2. Позвольте пользователю изменить данные через ввод.
3. Добавьте проверку: если пользователь не ввел данные, программа выводит сообщение об ошибке.'''


def checkData():
    profile = {}
    while True:
        usrName = input("Введите имя: ")

        if usrName.strip():
            profile["Имя пользователя"] = usrName
            print(f"Вы ввели: {usrName}")
            break
        else:
            print("Вы ввели пустые данные об имени. Попробуйте еще раз.")

    while True:
        profession = str(input("Введите профессию: "))

        if profession.strip():
            profile["Профессия"] = profession
            print(f"Вы ввели: {profession}")
            break
        else:
            print("Вы ввели пустые данные о профессии. Попробуйте еще раз.")

    while True:
        favoriteTestTool = str(input("Введите любимый инструмент для тестирования: "))

        if favoriteTestTool.strip():
            profile["Любимый инструмент для тестирования"] = favoriteTestTool
            print(f"Вы ввели: {favoriteTestTool}")
            break
        else:
            print("Вы ввели пустые данные о любимом инструменте для тестирования. Попробуйте еще раз.")
    return profile


original_profile = checkData()

changeData = input("Хотите изменить данные? Если да, то введите да или ok. Если нет, нажмите Enter: ")

if changeData.strip().lower() == "да" or "ok":
    new_profile = checkData()
    original_profile.update(new_profile)
    print("Данные изменены")
else:
    print("Изменения завершены")

print(f"Итоговые данные: {original_profile}")
