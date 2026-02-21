letters = ["d", "a", "c", "b"]
letters.sort()
print(letters)

counts = [100, 50, 200, 10]
counts.sort(reverse=True)
print(counts)

letters.sort(key = str.lower)
print(letters)

letters.reverse()
print(letters)

prices = [5.5, 2.1, 9.9]
prices.sort()
print(prices)
