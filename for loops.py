fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "Python":
  print(x)

for x in range(0, 5):
  print(x)

adj = ["red", "big"]
fruits = ["apple", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

prices = [10, 25, 5, 12]
total = 0
for p in prices:
    total += p
print(f"Total price: ${total}")