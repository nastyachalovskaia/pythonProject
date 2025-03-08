student = {"имя": "Елена", "возраст": 19, "оценка": 3.8}
key = "возраст"
isKeyPresent = key in student

if isKeyPresent:
    print(f"Ключ {key} найден в словаре")
else:
    print(f"Ключ {key} не найден в словаре")
