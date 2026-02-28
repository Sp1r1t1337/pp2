fruits = ["apple", "banana", "cherry"]
it = iter(fruits)
for x in it:
    print(x)

names = ("Alice", "Bob", "Charlie")
it_names = iter(names)
for name in it_names:
    print("User:", name)

msg = "PYTHON"
it_msg = iter(msg)
for char in it_msg:
    print(char)

nums = [1, 2, 3, 4, 5]
it_nums = iter(nums)
while True:
    try:
        print(next(it_nums))
    except StopIteration:
        break

vals = {100, 200, 300}
it_vals = iter(vals)
for v in it_vals:
    print("Value:", v)
