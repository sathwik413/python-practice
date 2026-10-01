import sys

# print the name
print("Hello, my name is", sys.argv[1])

# print the error message
try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")

# use exactly one argument
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1])

# using sys.exit()
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello, my name is", sys.argv[1])
