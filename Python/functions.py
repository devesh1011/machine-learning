def say_hello(name="World"):
    """This is a function that takes a string input and says hello to the user"""
    print(f"Hello! {name}")

name = input("What's your name? ")

say_hello(name)

# function with multiple positional args
def func_multiple_args(*args):
    return args
 
# function with multiple keyword arguments
def func_multiple_keyword_args(**kwargs):
    return kwargs

# lambda functions 
# syntax
# lambda parameters: values to return

lambda name: print("Hello!", name)