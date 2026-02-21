points = [(1, 2), (4, 1), (5, -1), (2, 3)]
points_sorted = sorted(points, key=lambda x: x[1])
print(points_sorted)

students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
by_age = sorted(students, key=lambda s: s[1])
print(by_age)

products = {"Apple": 50, "Banana": 10, "Orange": 30}
sorted_items = sorted(products.items(), key=lambda x: x[1])
print(sorted_items)

words = ["banana", "Pie", "apple", "Cherry"]
case_insensitive = sorted(words, key=lambda x: x.lower())
print(case_insensitive)

ids = ["id10", "id2", "id30", "id1"]
numeric_sort = sorted(ids, key=lambda x: int(x[2:]))
print(numeric_sort)
