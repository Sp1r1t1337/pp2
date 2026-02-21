status = 404

match status:
    case 200:
        print("Success")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown Status")

day = "Saturday"
match day:
    case "Saturday" | "Sunday":
        print("It is the weekend")
    case _:
        print("It is a workday")

point = (0, 5)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y-axis at {y}")
    case (x, 0):
        print(f"X-axis at {x}")

command = "quit"
match command:
    case "load":
        print("Loading data...")
    case "save":
        print("Saving data...")
    case "quit":
        print("Exiting program")

color = "red"
match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Caution")
    case "green":
        print("Go")
