def list_friends(*friends):
    print("My best friend is " + friends[0])

list_friends("Mark", "Dave", "Sara")

def multiply_all(*nums):
    result = 1
    for n in nums:
        result *= n
    return result

print(multiply_all(2, 3, 4))

def save_user(**data):
    print("Saving user: " + data["username"])

save_user(username="dev_pro", email="dev@test.com")

def build_pc(**parts):
    for part, name in parts.items():
        print(part + ": " + name)

build_pc(CPU="Intel i9", GPU="RTX 4090", RAM="32GB")

def master_func(*args, **kwargs):
    print(args)
    print(kwargs)

master_func(1, 2, mode="Turbo", active=True)
