ages = [5, 12, 17, 18, 24, 32]
adults = list(filter(lambda x: x >= 18, ages))
print(adults)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

words = ["apple", "kiwi", "banana", "pear"]
long_words = list(filter(lambda w: len(w) > 4, words))
print(long_words)

scores = [45, 88, 72, 30, 95]
passing = list(filter(lambda s: s > 50, scores))
print(passing)

mixed = [0, 1, False, True, "Hello"]
truthy = list(filter(lambda x: bool(x), mixed))
print(truthy)
