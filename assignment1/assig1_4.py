#4] Write a Python function to find the maximum of three numbers.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))


def find_maximum(num1, num2, num3):
    max = num1
    if num2 > max:
        max = num2
    if num3 > max:
        max = num3
    return max


maximum = find_maximum(num1, num2, num3)
print(f"The maximum number from this {num1}, {num2}, and {num3} is {maximum}")
