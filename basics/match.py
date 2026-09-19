# simple value matching
name = input("What's your name? ")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who? ")


# structural pattern matching
point = (0, 5)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"On the y-axis at {y}")
    case (x, 0):
        print(f"On the x-axis at {x}")
    case (x, y):
        print(f"Somewhere at ({x}, {y})")
