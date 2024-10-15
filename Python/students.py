# using csv files

# with open("./text_files/students.csv") as file:
#     for line in file:
#         name, age = line.rstrip().split(",")
#         print(f"{name} is {age} years old")


# sorting data by storing in the dictionary
students = []
import csv
    
# with open("./text_files/students.csv") as file:
#     reader = csv.reader(file)

#     for name, age in reader:
#         students.append({"name": name, "age": age})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is {student['age']} years old")

name = input("What's your name? ")
age = int(input("What's your age? "))

with open("./text_files/students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age"])
    writer.writerow({"name": name, "age": age})        
