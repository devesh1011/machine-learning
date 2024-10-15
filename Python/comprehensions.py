# dict comprehensions

students = ["Devesh", "Naushad", "Amit", "Rohit", "Rahul", "Monika", "Jahanvi"]

courses = {student: "B.Sc" for student in sorted(students)}

print(courses)

# enumerate --> enumerate(iterable, start=0)

for student in enumerate(students, 1):
    print(student)

# list comprehensions

n: int = int(input("Enter the even numbers you want to store upto: "))

even_nums = [num for num in range(n) if num % 2 == 0]  # list comprehension

print(*even_nums)
