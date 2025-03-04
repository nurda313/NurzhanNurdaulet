import json

person = {
    "name": "Ali",
    "age": 15,
    "city": "Almaty"
}

json_data = json.dumps(person)  # Преобразуем словарь в JSON
print(json_data)
