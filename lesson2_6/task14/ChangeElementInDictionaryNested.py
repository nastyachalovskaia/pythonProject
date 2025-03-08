students = [
    {"name": "Сергей", "age": 33},
    {"name": "Макар", "age": 31}
]

def update_age(students, name, newAge):

    for student in students:

        if student["name"] == name:
            student["age"] = newAge
            return

update_age(students, "Сергей", 34)

print(students)

