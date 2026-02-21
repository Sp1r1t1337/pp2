set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1.update(set2)
print(set1)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a.intersection(b)
print(c)

d = a.symmetric_difference(b)
print(d)

e = a.difference(b)
print(e)
