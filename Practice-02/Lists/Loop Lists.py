names = ["Alice", "Bob", "Charlie"]
for x in names:
    print(x)

for i in range(len(names)):
    print(names[i])

j = 0
while j < len(names):
    print(names[j])
    j += 1

[print(x) for x in names]

scores = [80, 90]
for s in scores:
    print(s)
