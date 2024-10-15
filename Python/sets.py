students = [
    {"name": "Devesh", "class": "bsc"},
    {"name": "Ankit", "class": "Btech"},
    {"name": "Naushad", "class": "bsc"},
    {"name": "ABC", "class": "bba"}
]

# classes = []

# for student in students:
#     if student["class"] not in classes:
#         classes.append(student["class"])

# for _class in sorted(classes):
#     print(_class)


# Better way
classes = set()
for student in students:
    classes.add(student["class"])

for _class in sorted(classes):
    print(_class)