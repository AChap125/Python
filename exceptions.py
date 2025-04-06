def square_number():
    while True:
        try:
            number = input("Enter a number to square: ")
            squared_number = int(number) ** 2
            print(f"The square of {number} is {squared_number}")
            break
        except ValueError:
            print(f"Error: '{number}' is not a valid number")

square_number()