# Step 1: Prompt the user for input
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

# Step 2: Perform logical comparisons and display results

# AND operator examples
print(f"Both numbers greater than 0: {num1 > 0 and num2 > 0}")
print(f"Both numbers greater than 100: {num1 > 100 and num2 > 100}")

# OR operator examples
print(f"Either number is even? {num1 % 2 == 0 or num2 % 2 == 0}")
print(f"Either number is less than 100? {num1 < 100 or num2 < 100}")

# NOT operator examples
print(f"num1 is not equal to num2: {not num1 == num2}")
print(f"num1 is not 0: {not num1 == 0}")