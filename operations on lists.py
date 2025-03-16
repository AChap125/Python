available_seats = list(range(1, 21))
def display_seats():
    print("\nAvailable Seats:")
    print(available_seats)
def select_seat():
    while True:
        try:
            seat_number = int(input("\nEnter the seat number you'd like to purchase (or enter '0' to finish): "))
            if seat_number == 0:
                print("Thank you for your purchase! Exiting the program.")
                return False 
            elif seat_number not in available_seats:
                print("Invalid selection. Please choose a valid seat number.")
            else:
                return seat_number
        except ValueError:
            print("Invalid input. Please enter a number.")
print("Welcome to the Ticket Sales System!")
while True:
    display_seats()
    seat = select_seat()
    if not seat:
        break
    available_seats.remove(seat)
    print(f"Seat {seat} has been successfully booked!")
    if not available_seats:
        print("All seats have been sold. Thank you for your purchases!")
        break