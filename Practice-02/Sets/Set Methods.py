x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y)
print(z)

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
print(a.issubset(b))

print(b.issuperset(a))

x.discard("banana")
print(x)

res = x.copy()
print(res)
