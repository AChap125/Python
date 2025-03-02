print("Budget Breakdown Calculator")

total_budget = float(input("Enter your total monthly budget (net income): $"))

housing = float(input("Enter amount spent on Housing (rent or mortgage): $"))
utilities = float(input("Enter amount spent on Utilities: $"))
groceries = float(input("Enter amount spent on Groceries: $"))
transportation = float(input("Enter amount spent on Transportation: $"))
health_care = float(input("Enter amount spent on Health Care: $"))
personal_care = float(input("Enter amount spent on Personal Care: $"))
clothing = float(input("Enter amount spent on Clothing: $"))
debt = float(input("Enter amount spent on Debt: $"))

housing_percent = (housing / total_budget) * 100
utilities_percent = (utilities / total_budget) * 100
groceries_percent = (groceries / total_budget) * 100
transportation_percent = (transportation / total_budget) * 100
health_care_percent = (health_care / total_budget) * 100
personal_care_percent = (personal_care / total_budget) * 100
clothing_percent = (clothing / total_budget) * 100
debt_percent = (debt / total_budget) * 100

print("\n--- Budget Breakdown ---")
print(f"Housing: {housing_percent:.2f}%")
print(f"Utilities: {utilities_percent:.2f}%")
print(f"Groceries: {groceries_percent:.2f}%")
print(f"Transportation: {transportation_percent:.2f}%")
print(f"Health Care: {health_care_percent:.2f}%")
print(f"Personal Care: {personal_care_percent:.2f}%")
print(f"Clothing: {clothing_percent:.2f}%")
print(f"Debt: {debt_percent:.2f}%")

total_spent = (
    housing + utilities + groceries + transportation +
    health_care + personal_care + clothing + debt
)
total_percent = (total_spent / total_budget) * 100
print(f"\nTotal Spent: {total_percent:.2f}% of your budget")

print("\nThank you for using the Budget Breakdown Calculator!")