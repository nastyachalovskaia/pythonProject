num = int(input("Введите число: "))
result = num > 0 and num % 2 == 0
if result:
    print(f"Число {num} является положительным и чётным")
else:
    print(f"Число {num} не подходит под условие")