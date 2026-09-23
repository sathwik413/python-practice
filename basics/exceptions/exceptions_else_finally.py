# using try and except
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

# using else
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

# using finally
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
finally:
    print("This prints no matter what")

# using finally by deliberately placing wrong error type
try:
    int("abc")
except TypeError:
    print("x is not an integer")
finally:
    print("This prints no matter what")
