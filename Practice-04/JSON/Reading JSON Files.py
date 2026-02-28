import json

with open("config.json", "r") as file:
    data = json.load(file)
    print(data["theme"])

with open("users.json", "r") as f:
    user_list = json.load(f)
    print(len(user_list))

try:
    with open("missing.json", "r") as f:
        content = json.load(f)
except FileNotFoundError:
    print("File not found.")

with open("settings.json", "r") as f:
    prefs = json.load(f)
    print(prefs.get("volume"))

with open("data.json", "r") as f:
    numbers = json.load(f)
    print(numbers["items"])
