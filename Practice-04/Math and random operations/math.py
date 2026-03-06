#1
def square_generator(n):
    for i in range(1, n + 1):
        yield i ** 2
n = 5
for sq in square_generator(n):
    print(sq)  # Выведет 1, 4, 9, 16, 25


#2
def even_generator(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield str(i)

n = int(input("Введите n: "))
print(", ".join(even_generator(n)))


#3
def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input("Введите диапазон (n): "))
for num in divisible_by_3_and_4(n):
    print(num)


#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
start, end = 3, 7
print(f"Квадраты от {start} до {end}:")
for val in squares(start, end):
    print(val)

#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
for x in countdown(5):
    print(x)  # Выведет 5, 4, 3, 2, 1, 0
