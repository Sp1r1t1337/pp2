
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


for x in "banana":
    print(x)


for x in fruits:
    print(x)
    if x == "banana":
        break


for x in fruits:
    if x == "banana":
        continue
    print(x)


for x in range(6):
    print(x)


for x in range(2, 6):
    print(x)


for x in range(2, 30, 3):
    print(x)


for x in range(6):
    print(x)
else:
    print("Finally finished!")


for x in range(6):
    if x == 3: break
    print(x)
else:
    print("This will not print")


adj = ["red", "big", "tasty"]
for x in adj:
    for y in fruits:
        print(x, y)


for x in [0, 1, 2]:
    pass
print("Loop bypassed with pass")
