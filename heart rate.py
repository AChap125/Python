time_slots = ["Morning", "Midday", "Afternoon", "Evening"]
heart_rates = []
for time in time_slots:
    while True:
        try:
            heart_rate = int(input(f"Enter your heart rate (in BPM) in the {time}: "))
            if heart_rate < 0:
                print("Please enter a non-negative number.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    heart_rates.append([time, heart_rate])
total = 0
for entry in heart_rates:
    total += entry[1]  
average = total / len(time_slots)  
print("\nHeart Rate Readings:")
for entry in heart_rates:
    print(f"In the {entry[0]}, your heart rate was: {entry[1]} BPM")
print(f"\nAverage heart rate today: {average:.2f} BPM")