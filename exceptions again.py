class NotNumericError(Exception):
    """Exception raised when input is not numeric."""
    def __init__(self, value):
        self.value = value
        self.message = f"'{value}' is not a valid number. Enter numeric digits only."
        super().__init__(self.message)

def get_numeric_input():
    try:
        user_input = input("Enter a number: ")
        
        if not user_input.isnumeric():
            raise NotNumericError(user_input)
            
    except NotNumericError as e:
        print(f"Invalid input: {e}")
        return get_numeric_input()
        
    else:
        print(f"Thanks, You entered the valid number: {user_input}")
        return int(user_input)
        
    finally:
        print("Input validation process completed.")

if __name__ == "__main__":
    print("Number Input Program")
    number = get_numeric_input()
    print(f"Program received the number: {number}")