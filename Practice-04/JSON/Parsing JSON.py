import json

json_data = '{"brand": "Ford", "model": "Mustang", "year": 1964}'
python_dict = json.loads(json_data)
print(python_dict["brand"])

user_json = '{"id": 42, "active": true, "roles": ["admin", "editor"]}'
user_dict = json.loads(user_json)
print(user_dict["roles"][0])

list_json = '[10, 20, 30, 40]'
numbers = json.loads(list_json)
print(sum(numbers))

nested_json = '{"office": {"floor": 5, "room": "A1"}}'
office_data = json.loads(nested_json)
print(office_data["office"]["room"])

json_with_null = '{"name": "Bob", "middle_name": null}'
python_obj = json.loads(json_with_null)
print(python_obj["middle_name"])
