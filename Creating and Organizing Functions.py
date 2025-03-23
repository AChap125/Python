def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial(n-1)
    else:
        return n * factorial(n - 1)
def main():
    # asks for a whole number
    try:
        n = int(input("Enter a non-negative integer: "))
        if n < 0:
            print("Please enter a non-negative integer.")
        else:
            # calculates the factorial using the recursive function
            result = factorial(n)
            # displays the result
            print(f"The factorial of {n} is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
# this runs the main function
if __name__ == "__main__":
    main()