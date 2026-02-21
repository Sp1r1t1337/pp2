def calculate_area(radius):
    return 3.14 * (radius ** 2)

print(calculate_area(5))

def convert_to_km(miles):
    return miles * 1.609

dist = convert_to_km(10)
print(dist)

def check_login(status):
    return status == "Success"

print(check_login("Success"))

def full_name(first, last):
    return first + " " + last

print(full_name("John", "Doe"))

def find_max(a, b):
    if a > b:
        return a
    return b

print(find_max(15, 25))
