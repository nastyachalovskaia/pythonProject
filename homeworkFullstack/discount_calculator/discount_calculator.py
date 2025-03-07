# **Задание:**
#
# 1. Запросите у пользователя сумму покупки.
# 2. Запросите процент скидки.
# 3. Рассчитайте сумму со скидкой и сколько пользователь сэкономит.
# 4. Округлите сумму к ближайшему целому числу и выведите результат.

totalSum = float(input(f"Введите сумму покупки "))
discount = int(input(f"Введите процент скидки "))

sumWithDiscount = ((totalSum * discount)/100)
economy = sumWithDiscount
result = round(totalSum - sumWithDiscount)

print(f"Вы экономите {economy} и заплатите {result} ")

