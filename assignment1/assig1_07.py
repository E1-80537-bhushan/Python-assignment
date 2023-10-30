"""Using for loop, write and run a Python program to find factorial from 0 to
10."""


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


for num in range(11):
    fact = factorial(num)
    print(f"The factorial of {num} is {fact}")
