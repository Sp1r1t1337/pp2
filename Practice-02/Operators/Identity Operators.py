list_a = [1, 2, 3]
list_b = [1, 2, 3]
print(list_a is list_b)

print(list_a is not list_b)

list_c = list_a
print(list_a is list_c)

x = ["apple"]
y = ["apple"]
print(x is y)

z = x
print(z is not y)
