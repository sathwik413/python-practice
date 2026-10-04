# Here, name is stored in the memory and once the program ends then it is no longer available
name = input("What's your name? ")
print(f"Hello, {name}")


# for multiple names to be inputted
names = []

for _ in range(3):
    name = input("What's your name? ")
    names.append(name)


# can be further modified as
names = []

for _ in range(3):
    names.append(input("What's your name? "))


# to print the three names that are stored in the list
names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in names:
    print(f"Hello, {name}")


# to print the greeting in sorted manner
names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"Hello, {name}")


# still here the names are stored in memory and are lost the moment the program ends. File I/O helps us store the data so that it can also be used later.
