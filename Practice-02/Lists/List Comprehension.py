data = [1, 2, 3, 4, 5]
new_data = [x * 10 for x in data]
print(new_data)

filtered = [x for x in data if x > 2]
print(filtered)

words = ["sun", "moon", "star"]
upper_words = [w.upper() for w in words]
print(upper_words)

zeros = [0 for x in range(4)]
print(zeros)

parity = ["Even" if x % 2 == 0 else "Odd" for x in data]
print(parity)
