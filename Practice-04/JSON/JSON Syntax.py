import json

json_string = '{"name": "Alice", "age": 25, "is_student": true}'

data = {
    "string": "value",
    "number": 100,
    "list": [1, 2, 3],
    "boolean": False,
    "null_val": None
}

print(json.dumps(data, indent=4))

complex_json = {
    "id": 1,
    "meta": {"created": "2026-02-28"},
    "tags": ["python", "json"]
}
print(complex_json["meta"]["created"])

invalid_example = "Dictionaries use single quotes in Python, but JSON requires double quotes."
