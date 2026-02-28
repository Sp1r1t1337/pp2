import json

person = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(person)
print(json_string)

numbers = [1, "apple", True, None]
print(json.dumps(numbers))

data = {"id": 1, "task": "Clean room"}
print(json.dumps(data, indent=2))

scores = {"math": 90, "science": 85}
print(json.dumps(scores, separators=(". ", " = ")))

unordered = {"z": 1, "a": 10, "m": 5}
print(json.dumps(unordered, sort_keys=True))
