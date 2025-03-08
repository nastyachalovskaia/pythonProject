# **Задание:**
#
# 1. Запросите у пользователя сумму покупки.
# 2. Запросите процент скидки.
# 3. Рассчитайте сумму со скидкой и сколько пользователь сэкономит.
# 4. Округлите сумму к ближайшему целому числу и выведите результат.

total_sum = float(input(f"Введите сумму покупки "))
discount = int(input(f"Введите процент скидки "))

total_discount = ((total_sum * discount) / 100)
economy = total_discount
result = round(total_sum - total_discount)

print(f"Вы экономите {economy} и заплатите {result} ")
