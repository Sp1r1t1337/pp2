numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

prices = [10, 20, 30]
taxed = list(map(lambda p: p * 1.1, prices))
print(taxed)

names = ["alice", "bob", "charlie"]
upper_names = list(map(lambda n: n.upper(), names))
print(upper_names)

celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)

str_nums = ["1", "2", "3"]
ints = list(map(lambda x: int(x), str_nums))
print(ints)
