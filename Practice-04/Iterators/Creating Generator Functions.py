def my_numbers(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for x in my_numbers(3):
    print(x)

def even_nums(limit):
    n = 0
    while n < limit:
        yield n
        n += 2

print(list(even_nums(10)))

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(5)))

def reverse_str(my_str):
    for i in range(len(my_str)-1, -1, -1):
        yield my_str[i]

for char in reverse_str("ABC"):
    print(char)

def square_gen(nums):
    for n in nums:
        yield n * n

for s in square_gen([1, 2, 3]):
    print(s)
