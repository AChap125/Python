# Ask the user for their age and convert the input to an integer
age = int(input("How old are you? "))

# Check if the user is old enough to drive
if age >= 16:
    print("You are old enough to drive.")
else:
    print("You are not old enough to drive.")

# Check if the user can vote
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")

# Check if the user can legally buy alcohol
if age >= 21:
    print("You can buy alcohol legally.")
else:
    print("You cannot buy alcohol legally.")

# Check if the user is eligible for a senior discount 
if age >= 65:
    print("You are eligible for the senior discount.")
else:
    print("You are not eligible for the senior discount.")