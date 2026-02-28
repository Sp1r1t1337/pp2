numbers = [10, 20, 30, 40, 50]
my_iter = iter(numbers)
print(next(my_iter))

colors = ("Red", "Green", "Blue")
it = iter(colors)
print(next(it))
print(next(it))

word = "CODE"
it_str = iter(word)
print(next(it_str))

data = {1, 2, 3}
it_set = iter(data)
print(next(it_set))

prices = {"apple": 1, "banana": 2}
it_dict = iter(prices)
print(next(it_dict))
