#Find and display the largest number of a list without using built-in function max(). Your program should
#ask the user to input values in list from keyboard.

l1=[]
n=int(input("enter the number of element you want : "))

for i in range(n):
    element=int(input("enter the list element"))
    l1.append(element)
print(l1)

maximum = l1[0]

for element in l1:
    if element > maximum:
        maximum = element


print(f"maximum number is {maximum}")
