# x = int(input('Enter x: '))
# y = int(input("Enter y: "))

# if x > y:
#     print("if block excuted")
#     print("X is greater than y")
# elif x < y:
#     print("elif block excuted")
#     print("x is smaller than y")
# else:
#     print("else block excuted")
#     print("x is equal to y")

def is_even(n): 
    return (n % 2 == 0)

num = int(input("Enter the number: "))

if is_even(num):
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# match statement
day_in_no = int(input("enter the day no: "))

match day_in_no:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")

