num = int(input("Введите число: "))
result = 0 <= num <= 100

if result:
    print(f"Число {num} находится в пределах диапазона от 0 до 100")
else:
    print(f"Число {num} выходит за пределы диапазона от 0 до 100")
