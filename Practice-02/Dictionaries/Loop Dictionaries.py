data = {"a": 1, "b": 2, "c": 3}
for x in data:
    print(x)

for x in data:
    print(data[x])

for x in data.values():
    print(x)

for x, y in data.items():
    print(x, y)

for x in data.keys():
    print(x)
