frozen = frozenset(["CPU", "GPU", "RAM"])
print(frozen)

points = frozenset([1.5, 2.5, 3.5])
print(points)

# frozen.add("SSD") would result in an error
print("GPU" in frozen)

print(len(frozen))

vowels = frozenset(("a", "e", "i", "o", "u"))
print(vowels)
