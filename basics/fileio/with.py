# if we forget to close the file with file.close() then it may result in data loss we can fix this by using "with"
name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")


# now instead of writing to names.txt we can print using the data stored in it
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line)


# when run you can see a blank line in between each line of text because we used \n while storing names we can fix that using rstrip()
# we can also run the program without "r" as the argument is by default set to "r"
with open("names.txt") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line.rstrip())


# we can simplify the code into
with open("names.txt") as file:
    for line in file:
        print("Hello,", line.rstrip())


# to print them in sorted manner
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print("Hello,", name)
