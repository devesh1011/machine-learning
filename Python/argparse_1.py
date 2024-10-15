import argparse
import sys


if len(sys.argv) == 1:
    print("Meow")

elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("Meow")
else:
    print("Usage: firstProgram.py")

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="Number of times to meow", default=1, type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")

# argparse is used to interact with command line more easily 

# argparse is a Python library in the standard library's argparse module, which provides a way to easily parse command-line arguments and options. It allows you to define and parse command-line arguments for your Python scripts or programs, making it easier for users to interact with your code via the command line.