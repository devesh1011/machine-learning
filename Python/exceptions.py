# while True:
#     try:
#         x = int(input("What's x: "))
#     except ValueError:
#         print("You must enter a Integer value")
#     else:
#         break

# print(f"x is {x}")

# raise keyword - is used to raise exceptions by yourself in python

# pass keyword
def get_int():
    while True:
        try:
            return int(input("What's x: "))
        except ValueError:
            pass # ignores the statment

def main():
    x = get_int()
    print(f"x is {x}")

main()