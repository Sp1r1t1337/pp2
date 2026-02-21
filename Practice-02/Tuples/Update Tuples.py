coords = (10, 20)
temp_list = list(coords)
temp_list[1] = 50
coords = tuple(temp_list)
print(coords)

colors = ("Red", "Green")
y = list(colors)
y.append("Blue")
colors = tuple(y)
print(colors)

fruits = ("Apple", "Banana")
more_fruits = ("Orange",)
fruits += more_fruits
print(fruits)

data = (1, 2, 3)
z = list(data)
z.remove(2)
data = tuple(z)
print(data)

fixed_tuple = (100, 200)
del fixed_tuple
# print(fixed_tuple) would raise an error here
