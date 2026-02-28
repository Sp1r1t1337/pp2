nums = [1, 2, 3, 4]
squares = (x**2 for x in nums)
print(next(squares))
print(next(squares))

doubles = (x * 2 for x in range(10) if x % 2 == 0)
for d in doubles:
    print(d)

names = ["alice", "bob", "charlie"]
caps = (n.upper() for n in names)
print(list(caps))

prices = [10.5, 20.0, 15.75]
rounded = (round(p) for p in prices)
for r in rounded:
    print(r)

items = ("ID_" + str(i) for i in range(3))
for item in items:
    print(item)
