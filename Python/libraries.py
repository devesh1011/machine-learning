import random as rd
import statistics as stats

students = ["Ankit", "Devesh", "Prince", "Amit", "Naushad"]

# randint
num = rd.randint(1, 10)
print(num)

# randint
x = rd.choice(students)
print(x)
print()

# shuffle 
rd.shuffle(students)

for student in students:
    print(student, sep=", ")