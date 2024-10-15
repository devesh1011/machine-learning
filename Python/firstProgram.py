print("Hello World!")

name = input("What's your name? ")

# removing whitespaces from str
name = name.strip()
print(name)

# capitalize str
name = name.title()

# f literal 
print(f"Hello {name}")

name.split(".")
print(name)

# float
a = float (input("Enter a: "))
b = float (input("Enter b: "))

# z = round(a / b)

z = a / b

print(f"{z}")

print(f"{z:.2f}")  

# type hints -- defining what type the variable should be

# mypy is an optional static type checker for Python. It's a tool that helps you catch type-related errors and improve the reliability and maintainability of your Python code.

# def func(variable: type) -> return type:

def meow(n: int) -> None:
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    
    """
    for _ in range(n):
        print("Meow")

user_input: int = int(input("Enter the no of times you want to say meow: "))

meow(user_input)