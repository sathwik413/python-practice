# stores the name in names.txt but the second input overwrites the first input
name = input("What's your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()

# stores the second input along with first input but stored side by side without any spaces in between them
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(name)
file.close()


# "\n" ends the line and helps us store the data in the names.txt as we want
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
