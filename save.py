#цикл для списка

numbers = []
num1 = int(input())
num2 = int(input())
num2 = num2 + 1
for i in range(num1, num2):
    while True:
     number = int(input(f"Введите число {i}: "))
     numbers.append(number)  # Добавляем число в список
     break 

max_num = max(numbers)
min_num = min(numbers)
print(numbers)
print(max_num)
print(min_num)