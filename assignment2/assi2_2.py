#formula------>  	C.I. = Principal (1 + Rate)Time − Principal


def compound_interest(principal, rate, time, n):
    
    rate = rate / 100
    amount = principal * (1 + rate/n)**(n*time)

    interest_earned = amount - principal

    return amount, interest_earned


principal = 1000  
rate = 5  
time = 3  
n = 12  

result, interest = compound_interest(principal, rate, time, n)

print(f"Principal Amount: {principal}")
print(f"Annual Interest Rate: {rate}%")
print(f"Time (years): {time}")
print(f"Compounding : {n} times per year")
print(f"Total Amount after {time} years: ${result: 2f}")
print(f"Interest Earned: {interest:2f}")
