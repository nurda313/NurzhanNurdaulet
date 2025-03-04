my_dict = {"name": "Alice", "age": 25, "city": "New York"}
del my_dict["city"]
print("После удаления города:", my_dict)
my_dict.pop("age")
print("После удаления возраста:", my_dict)
my_dict.clear()
print("После очистки:", my_dict)