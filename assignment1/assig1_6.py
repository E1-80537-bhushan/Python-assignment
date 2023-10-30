#Write a Python function to calculate the factorial of a number (a non-negative integer).
#The function accepts the number as an argument.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a non-negative integer: "))
if number < 0:
    print("Please enter a non-negative integer.")
else:
    result = factorial(number)
    print(f"The factorial of {number} is {result}")
