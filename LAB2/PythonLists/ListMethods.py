fruits = ["apple", "banana", "cherry"]

# append() — добавляет элемент в конец списка
fruits.append("kiwi")
print("После добавления 'kiwi':", fruits)

# remove() — удаляет указанный элемент
fruits.remove("banana")
print("После удаления 'banana':", fruits)

# pop() — удаляет элемент по индексу
fruits.pop(1)  # Удаляет элемент с индексом 1
print("После удаления элемента с индексом 1:", fruits)

# reverse() — разворачивает список
fruits.reverse()
print("После разворота:", fruits)

# count() — подсчитывает количество вхождений элемента
fruits.append("apple")
print("Сколько раз 'apple' встречается в списке:", fruits.count("apple"))
