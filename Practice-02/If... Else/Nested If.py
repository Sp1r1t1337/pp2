num = 15

if num > 10:
    print("Above ten")
    if num > 20:
        print("And also above 20")
    else:
        print("But not above 20")

user_active = True
level = 2
if user_active:
    if level >= 2:
        print("Premium Access")

weather = "Rainy"
wind = "Strong"
if weather == "Rainy":
    if wind == "Strong":
        print("Stay indoors")

x = 5
if x > 0:
    if x < 10:
        print("Single digit positive")

auth = True
role = "Editor"
if auth:
    if role == "Editor":
        print("Can edit posts")
