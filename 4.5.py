from datetime import datetime, timedelta

def main():
    print("Welcome to the Age Calculator!")
    print("Please enter your birthday:")
    
    try:
        year = int(input("What year were you born? "))
        month = int(input("What month were you born (as a number)? "))
        day = int(input("What day of the month were you born? "))
        
        birthday = datetime(year, month, day)
        print(f"Your birthday is: {birthday.strftime('%Y-%m-%d')}")
        
        now = datetime.now()
        
        delta = now - birthday
        
        total_days = delta.days
        total_seconds = delta.total_seconds()
        
        years = total_days / 365.25
        
        months = years * 12
        
        weeks = total_days / 7
        
        
        hours = total_seconds / 3600
        
        minutes = total_seconds / 60
        
        print("\nYour age in different units:")
        print(f"Years: {years:.1f}")
        print(f"Months: {months:.1f}")
        print(f"Weeks: {weeks:.1f}")
        print(f"Days: {total_days}")
        print(f"Hours: {hours:,.1f}")
        print(f"Minutes: {minutes:,.1f}")
        
    except ValueError as e:
        print(f"Error: Invalid input. Please enter numbers for year, month, and day. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()