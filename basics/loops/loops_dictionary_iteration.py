students = {
    "Harry": "Gryffindor",
    "Hermione": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}
# prints both names & houses
for student in students:
    print(student, students[student], sep=", ")

# prints keys
for key in students.keys():
    print(key)

# prints values
for value in students.values():
    print(value)

# prints both keys and values
for key, value in students.items():
    print(key, value, sep=", ")
