#Write a function to return simple interest

p=int(input("enter the principal : "))
r=int(input("enter the Rate : "))
t=int(input("enter the time in year : "))

SI=(p*r*t)/100

print(f"simple interest is = {SI}")
