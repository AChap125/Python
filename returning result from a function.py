def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest
principal = float(input("Principal amount: "))
rate = float(input("Interest rate: "))
time = float(input("Time in years: "))
interest = calculate_interest(principal, rate, time)
print(f"The simple interest for ${principal:,.2f} at {rate}% over {time} years is ${interest:,.2f}.")