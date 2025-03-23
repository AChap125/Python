POUNDS_TO_KG = 0.453592
INCHES_TO_METERS = 0.0254
def calculate_bmi(weight_lb, height_in):
    """
    Calculate BMI based on weight in pounds and height in inches.
    Converts weight and height to metric units, then calculates BMI.
    """
    weight_kg = weight_lb * POUNDS_TO_KG
    height_m = height_in * INCHES_TO_METERS
    bmi = weight_kg / (height_m ** 2)
    return bmi
def categorize_bmi(bmi):
    """
    Categorize BMI into underweight, normal weight, overweight, or obese.
    """
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 25:
        return "normal weight"
    elif 25 <= bmi < 30:
        return "overweight"
    else:
        return "obese"
def main():
    """
    Main function to prompt user for weight and height, calculate BMI, and display results.
    """
    weight_lb = float(input("Enter your weight in pounds: "))
    height_in = float(input("Enter your height in inches: "))
    bmi = calculate_bmi(weight_lb, height_in)
    category = categorize_bmi(bmi)
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are in the {category} category.")
if __name__ == "__main__":
    main()