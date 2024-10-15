def main():
    n = int(input("What's n? "))

    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑" * i
    
if __name__ == "__main__":
    main()

# yield helps the machine give you numbers one at a time, taking breaks in between, which is really helpful when you have a lot of numbers to deal with. It's like a friendly robot that doesn't overwhelm you with all the numbers at once, but instead gives them to you one by one.