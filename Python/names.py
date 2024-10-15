# name = input("What's your name? ")

# with open("./text_files/names.txt", "a") as file:
#     file.write(f"{name}\n")

# with open("./text_files/names.txt", 'r') as read_file:
#     for line in read_file:
#         print(f"hello, {line.rstrip()}")

names = []

with open("./text_files/names.txt") as file:
    for line in file:
        names.append(line.strip())

for name in sorted(names):
    print(f"Hello, {name}")

# using csv files    