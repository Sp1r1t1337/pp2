def welcome_user(name):
    print("Welcome, " + name)

welcome_user("Alice")

def power_level(name, level):
    print(name + " is at level " + str(level))

power_level("Bob", 9000)

def set_destination(city = "New York"):
    print("Heading to " + city)

set_destination("London")
set_destination()

def car_info(brand, model):
    print("Car: " + brand + " " + model)

car_info(model = "Model S", brand = "Tesla")

def process_list(items):
    for x in items:
        print("Item:", x)

process_list(["Pen", "Paper", "Ink"])
