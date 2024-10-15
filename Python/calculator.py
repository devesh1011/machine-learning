def add(num1=0, num2=0):
    return num1 + num2

def subtract(num1=0, num2=0):
    print(num1 - num2)

def multiply(num1=1, num2=1):
    print(num1 * num2)

def divide(dividend=0, divisor=1):
    print(dividend / divisor)
            
def main():
    print("Welcome to my calculator program😊")
    play_cal = True
    while play_cal:
        operation = input("Enter the operation you want to perform.Choose from (+, -, *, /) or to exit Type 'n': ").lower()

        if operation == 'n':
            play_cal = False
            break

        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        match operation:
            case "+":
                add(num1, num2)
            case "-":
                subtract(num1, num2)
            case "*":
                multiply(num1, num2)
            case "/":
                divide(num1, num2)
            case _:
                print("Please enter a valid operator!")

if __name__ == "__main__":
    main()