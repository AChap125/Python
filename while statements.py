# number of bottles
bottles = 99

# Use a while loop to iterate through the bottles
while bottles > 0:
    # Handle plural vs. singular for the current number of bottles
    if bottles == 1:
        print(f"{bottles} bottle of beer on the wall")
        print(f"{bottles} bottle of beer")
    else:
        print(f"{bottles} bottles of beer on the wall")
        print(f"{bottles} bottles of beer")

    # Take one bottle down
    print("Take one down, pass it around")
    bottles -= 1

    # Handle plural vs. singular for the remaining bottles
    if bottles == 1:
        print(f"{bottles} bottle of beer on the wall!\n")
    elif bottles == 0:
        print("No bottles of beer on the wall!\n")
    else:
        print(f"{bottles} bottles of beer on the wall!\n")