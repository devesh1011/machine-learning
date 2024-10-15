for _ in range(3):
    print("Hello World!")

i = 0
while i < 3:
    print("Hello World!")
    i += 1

# more pythonic - not recommended
print("meow\n" * 3, end="")

def meow(n):
    if n < 0:
        print("Enter a posive number")

    for _ in range(2):
        print("Meow")

# meow_times = int(input("How many times you want your cat to meow? "))
# meow(meow_times)

# list 
students = ["Ankit", "Devesh", "Prince", "Amit", "Naushad"]

students.remove("Ankit")
students.sort()

print(students)

# dict
students_dict = {
    1: "Devesh",
    2: "Ankit",
    3: "Prince",
    4: "Naushad"
}

for n in students_dict:
    print(n, students_dict[n], sep=" = ")

# pattern printing

def print_sqaure(size):
    for i in range(size):
        for j in range(size):
            print("#", end=" ")
        print()

print_sqaure(3)
    
