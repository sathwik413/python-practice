students = [
    {"name": "Harry", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")


# print only the name of students that belong to Gryffindor
for student in students:
    if student["house"] == "Gryffindor":
        print(student["name"])
