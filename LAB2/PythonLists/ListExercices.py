numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = sum(x for x in numbers if x % 2 == 0)  # Суммируем только четные числа
print("Сумма четных чисел:", even_sum)
