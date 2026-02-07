status = 404

match status:
    case 200:
        print("Success")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")

day = "Sunday"

match day:
    case "Monday":
        print("Back to work")
    case "Friday":
        print("Weekend is near")
    case _:
        print("Just another day")

fruit = "Apple"

match fruit:
    case "Apple" | "Banana" | "Cherry":
        print("This is a fruit")
    case _:
        print("Unknown food")

number = 15

match number:
    case n if n > 0:
        print("Positive number")
    case n if n < 0:
        print("Negative number")
    case 0:
        print("It is zero")

command = ["move", "left"]

match command:
    case ["stop"]:
        print("Stopping now.")
    case ["move", direction]:
        print(f"Moving in direction: {direction}")