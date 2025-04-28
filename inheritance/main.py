from employee import ProductionWorker # type: ignore

def main():
    print("Enter the following details of the Employee")
    print("--------------------------------------------")
    name = input("Enter Employee Name: ")
    number = input("Enter Employee Number: ")
    pay_rate = float(input("Enter Pay Rate: "))
    shift_number = int(input("Enter Shift Number (1 for Day, 2 for Night): "))

    worker = ProductionWorker(name, number, shift_number, pay_rate)

    print("-------------------------------------------------------")
    print("Details of Employee:")
    print("-------------------------------------------------------")
    print(f"Name: {worker.get_name()}")
    print(f"Employee Number: {worker.get_number()}")

    if worker.get_shift_number() == 1:
        shift = "Day"
    elif worker.get_shift_number() == 2:
        shift = "Night"
    else:
        shift = "Invalid shift number"

    print(f"Shift: {shift}")
    print(f"Pay Rate: {worker.get_hourly_pay_rate():.2f}")

if __name__ == "__main__":
    main()