my_set = {1, 2, 3, "apple"}
my_set.remove(2)
print("После удаления 2:", my_set)
my_set.discard("apple")
print("После удаления 'apple':", my_set)
my_set.pop()
print("После случайного удаления:", my_set)
my_set.clear()
print("После очистки:", my_set)