point = (4, 9, 2)
x, y, z = point
print(x, y, z)

names = ("Alice", "Bob", "Charlie", "David")
(first, second, *others) = names
print(first, second, others)

(start, *middle, end) = (1, 2, 3, 4, 5)
print(start, middle, end)

(*beginning, last) = ("a", "b", "c")
print(beginning, last)

colors = ("Red", "Blue")
(c1, c2) = colors
print(c1)
print(c2)
