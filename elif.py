# Prompt the user to enter their numeric grade
numeric_grade = float(input("Enter the numeric grade: "))

# Check if the grade is within the valid range (0 to 100)
if 0 <= numeric_grade <= 100:
    # Determine the letter grade based on the grading scale
    if numeric_grade >= 90:
        letter_grade = "A"
    elif numeric_grade >= 80:
        letter_grade = "B"
    elif numeric_grade >= 70:
        letter_grade = "C"
    elif numeric_grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    # Display the letter grade
    print(f"The letter grade is: {letter_grade}")
else:
    # Display an error message if the grade is outside the valid range
    print("Invalid grade. Please enter a number between 0 and 100.")