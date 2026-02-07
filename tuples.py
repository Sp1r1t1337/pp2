tuple = ("a", "b", "c")
print(tuple[2])

a = list(tuple)
a[0] = "d"
b = tuple(a)
print(b)

for x in tuple:
    print(x)

newtuple = (3, 9)
print(tuple + newtuple * 2)

i =tuple.count("a")
print(i)


