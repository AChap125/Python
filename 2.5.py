def main():
    import re  
    
    SYMBOLS = set('!@#$%&*')
    
    print("Welcome to Password Validator")
    print("Your password must meet the following requirements:")
    print("- 8 to 20 characters long")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one number")
    print("- At least one symbol (!@#$%&*)")
    
    while True:
        try:
            while True:
                password1 = input("\nEnter your password: ")
                
                if len(password1) < 8 or len(password1) > 20:
                    print("Password must be between 8 and 20 characters.")
                    continue
                
                if not any(char.isupper() for char in password1):
                    print("Password must contain at least one uppercase letter.")
                    continue
                
                if not any(char.islower() for char in password1):
                    print("Password must contain at least one lowercase letter.")
                    continue
                
                if not any(char.isdigit() for char in password1):
                    print("Password must contain at least one number.")
                    continue
                
                if not any(char in SYMBOLS for char in password1):
                    print("Password must contain at least one symbol (!@#$%&*).")
                    continue
                
                break 
            
            password2 = input("Confirm your password: ")
            
            if password1 == password2:
                print("\nSuccess! Your password has been set.")
                break
            else:
                print("Passwords do not match. Please try again.")
        
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    main()