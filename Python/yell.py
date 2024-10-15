def main():
    yell("This", "is", "devesh")

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

if __name__ == "__main__":
    main()

# map function takes a callback function which will work on the iterable and second argument as the iterable

# map Function:
# The map function applies a given function to each element of an iterable and returns an iterable containing the results of applying that function.
# It takes two arguments: a function and an iterable.
# The function is applied to each element of the iterable, and the result is collected in a new iterable.
# The length of the resulting iterable will be the same as the input iterable.

# filter function

filter_even_nums = filter(lambda n: n % 2 == 0, range(10))

print(*filter_even_nums)


# filter Function:
# The filter function, as the name suggests, filters elements from an iterable based on a given condition (a function that returns True or False).
# It also takes two arguments: a function and an iterable.
# The function is applied to each element, and only elements for which the function returns True are included in the output iterable.


# dict comprehensions

