days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
steps = []
for day in days:
    while True:
        try:
            step_count = int(input(f"How many steps did you take on {day}? "))
            if step_count < 0:
                print("Please enter a non-negative number.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    steps.append(step_count)
print("\nDaily Steps:")
for i in range(len(days)):
    print(f"{days[i]}: {steps[i]} steps")
total_steps = sum(steps)
print(f"\nTotal steps: {total_steps}")
average_steps = total_steps / len(steps)
print(f"Average steps: {average_steps:.0f}")