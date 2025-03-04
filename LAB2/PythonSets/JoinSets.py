set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print("Объединенное множество:", result)
set1.update(set2)
print("Множество после update():", set1)