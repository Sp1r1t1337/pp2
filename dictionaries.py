car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)

print(car["model"])

car["year"] = 2024  
car["color"] = "red"
print(car)

laptop = {"brand": "Apple", "model": "MacBook", "year": 2022}
laptop.pop("year")
print(laptop)

user = {"name": "Alice", "role": "Admin"}

for key, value in user.items():
    print(key, ":", value)


