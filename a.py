def multiply_numbers(numbers):
    result = 1  # Начинаем с 1, потому что это нейтральный элемент для умножения
    for number in numbers:
        result *= number  # Умножаем каждый элемент списка
    return result  # Возвращаем произведение

# Ввод чисел от пользователя
user_input = input("Введите числа через пробел: ")
numbers_list = [int(x) for x in user_input.split()]  # Преобразуем строку в список чисел

# Вызов функции и вывод результата
product = multiply_numbers(numbers_list)
print(f"Произведение чисел: {product}")
