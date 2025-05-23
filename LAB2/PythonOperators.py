# Арифметические операторы
print("Сложение:", 5 + 3)      # 8
print("Вычитание:", 10 - 4)    # 6
print("Умножение:", 6 * 2)     # 12
print("Деление:", 10 / 2)      # 5.0
print("Целочисленное деление:", 10 // 3)  # 3
print("Остаток от деления:", 10 % 3)      # 1
print("Степень:", 2 ** 3)      # 8

# Операторы сравнения
print("Равно (5 == 5):", 5 == 5)         # True
print("Не равно (5 != 3):", 5 != 3)      # True
print("Больше (5 > 3):", 5 > 3)          # True
print("Меньше (2 < 4):", 2 < 4)          # True
print("Больше или равно (5 >= 5):", 5 >= 5)  # True
print("Меньше или равно (3 <= 4):", 3 <= 4)  # True


# Логические операторы
x = True
y = False
print("Логическое И (True and False):", x and y)  # False
print("Логическое ИЛИ (True or False):", x or y)  # True
print("Логическое НЕ (not True):", not x)         # False


# Побитовые операторы
a = 5  # В двоичной системе это 0101
b = 3  # В двоичной системе это 0011
print("Побитовое И (5 & 3):", a & b)     # 1 (0001)
print("Побитовое ИЛИ (5 | 3):", a | b)   # 7 (0111)
print("Исключающее ИЛИ (5 ^ 3):", a ^ b) # 6 (0110)
print("Побитовое отрицание (~5):", ~a)   # -6
print("Сдвиг влево (2 << 2):", 2 << 2)   # 8
print("Сдвиг вправо (8 >> 2):", 8 >> 2)  # 2


# Присваивающие операторы
x = 10
x += 5  # x = x + 5
print("x после += 5:", x)  # 15

x -= 3  # x = x - 3
print("x после -= 3:", x)  # 12

x *= 2  # x = x * 2
print("x после *= 2:", x)  # 24

x /= 4  # x = x / 4
print("x после /= 4:", x)  # 6.0


# Операторы членства
fruits = ["apple", "banana", "cherry"]
print("'apple' in fruits:", "apple" in fruits)      # True
print("'grape' not in fruits:", "grape" not in fruits)  # True


# Операторы идентичности
a = [1, 2, 3]
b = a
print("a is b:", a is b)  # True (ссылаются на один объект)

c = [1, 2, 3]
print("a is c:", a is c)  # False (разные объекты в памяти)


