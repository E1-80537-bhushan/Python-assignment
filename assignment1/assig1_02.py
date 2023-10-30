"""
2] Write a program to accept a 4 digit number and
a. Display face value of each decimal digit
b. Display place value of each decimal digit
c. Display no in reverse order by changing decimal place values If user enters a 4 digit number 9361 outp
ut should be
a. 9 3 6 1
b. 9361 = 9 000 + 300 + 60 + 9
c. 1639
"""

number = input("Enter a 4-digit number: ")


if number.isdigit() and len(number) == 4:
    
    reversed_number = ""
    for digit in number:
        reversed_number = digit + " " + reversed_number
    print(f"a. {reversed_number.strip()}")

  
    formatted_number = ""
    for i, digit in enumerate(number):
        formatted_number += f"{digit}{'0' * (3 - i)} + "
    formatted_number = formatted_number[:-3] 
    print(f"b. {number} = {formatted_number}")

   
    reversed_formatted_number = ""

    for i, digit in enumerate(reversed(number)):
        reversed_formatted_number += f"{digit}{'0' * i} + "
    reversed_formatted_number = reversed_formatted_number[:-3]  
    print(f"c. {reversed_formatted_number}")
else:
    print("Please enter a valid 4-digit number.")

