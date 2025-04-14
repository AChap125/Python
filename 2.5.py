def main():
    import re
    
    SYMBOLS = {'!', '@', '#', '$', '%', '&', '*'}
    
    def validate_password(password):
        """Validate password against all criteria."""
        errors = []
        
        errors += ["Password must be 8-20 characters long."] if len(password) < 8 or len(password) > 20 else []
        
        errors += ["Password must contain at least one uppercase letter."] if not any(char.isupper() for char in password) else []
        
        errors += ["Password must contain at least one lowercase letter."] if not any(char.islower() for char in password) else []
        
        errors += ["Password must contain at least one number."] if not any(char.isdigit() for char in password) else []
        
        errors += ["Password must contain at least one symbol (!@#$%&*)."] if not any(char in SYMBOLS for char in password) else []
        
        return errors
    
    def get_valid_password():
        """Get a password that meets all criteria."""
        print("Welcome to Password Validator")
        print("Your password must meet the following requirements:")
        print("- 8 to 20 characters long")
        print("- At least one uppercase letter")
        print("- At least one lowercase letter")
        print("- At least one number")
        print("- At least one symbol (!@#$%&*)")
        
        password = input("\nEnter your password: ")
        errors = validate_password(password)
        
        def handle_errors(errors):
            print("\nInvalid password. Please fix the following:")
            for error in errors:
                print(f"- {error}")
            return get_valid_password()
        
        return password if not errors else handle_errors(errors)
    
    def confirm_password(password):
        """Confirm the password matches."""
        confirm = input("Confirm your password: ")
        return "Success! Your password has been set." if password == confirm else confirm_password(password)
    
    valid_password = get_valid_password()
    result = confirm_password(valid_password)
    print(result)

if __name__ == "__main__":
    main()