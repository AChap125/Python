def main_menu():
    while True:
        try:
            print("\n===== Customer Management System =====")
            print("1. Create a new entry")
            print("2. Display an entry by last name")
            print("3. Update an existing entry")
            print("4. Remove an entry")
            print("5. Quit")
            choice = int(input("Please enter your choice (1-5): "))
            if 1 <= choice <= 5:
                return choice
            print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check():
    try:
        with open("customer_list.txt", 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print("No existing customer data found. Starting new database.")
        return []

def save(customers):
    with open("customer_list.txt", 'w') as file:
        file.writelines(customers)
    print("Data saved successfully.")

def create():
    customers = check()
    print("\n--- Create New Customer ---")
    fname = input("First Name: ").strip()
    lname = input("Last Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    
    new_entry = f"{fname},{lname},{phone},{email}\n"
    customers.append(new_entry)
    save(customers)
    print(f"Added new customer: {fname} {lname}")

def read():
    customers = check()
    if not customers:
        print("No customers in database.")
        return
    
    search_name = input("\nEnter last name to search: ").strip().lower()
    found = False
    
    print("\nSearch Results:")
    for customer in customers:
        parts = customer.strip().split(',')
        if len(parts) >= 2 and search_name == parts[1].strip().lower():
            print(f"\nFirst Name: {parts[0]}")
            print(f"Last Name: {parts[1]}")
            print(f"Phone: {parts[2]}")
            print(f"Email: {parts[3]}")
            found = True
    
    if not found:
        print(f"No customers found with last name '{search_name}'.")

def update():
    customers = check()
    if not customers:
        print("No customers in database.")
        return
    
    search_name = input("\nEnter last name to update: ").strip().lower()
    updated = False
    
    for i, customer in enumerate(customers):
        parts = customer.strip().split(',')
        if len(parts) >= 2 and search_name == parts[1].strip().lower():
            print("\nCurrent Information:")
            print(f"1. First Name: {parts[0]}")
            print(f"2. Last Name: {parts[1]}")
            print(f"3. Phone: {parts[2]}")
            print(f"4. Email: {parts[3]}")
            
            try:
                field = int(input("\nWhich field to update? (1-4): "))
                if 1 <= field <= 4:
                    new_value = input(f"Enter new {['first name', 'last name', 'phone', 'email'][field-1]}: ").strip()
                    parts[field-1] = new_value
                    customers[i] = f"{','.join(parts)}\n"
                    save(customers)
                    print("Record updated successfully.")
                    updated = True
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Update cancelled.")
    
    if not updated:
        print(f"No customer found with last name '{search_name}'.")

def delete():
    customers = check()
    if not customers:
        print("No customers in database.")
        return
    
    search_name = input("\nEnter last name to delete: ").strip().lower()
    deleted = False
    
    for i, customer in enumerate(customers[:]):
        parts = customer.strip().split(',')
        if len(parts) >= 2 and search_name == parts[1].strip().lower():
            print("\nCustomer Found:")
            print(f"Name: {parts[0]} {parts[1]}")
            print(f"Phone: {parts[2]}")
            print(f"Email: {parts[3]}")
            
            confirm = input("\nAre you sure you want to delete? (y/n): ").strip().lower()
            if confirm == 'y':
                customers.pop(i)
                save(customers)
                print("Record deleted successfully.")
                deleted = True
                break
            else:
                print("Deletion cancelled.")
    
    if not deleted:
        print(f"No customer found with last name '{search_name}'.")

def main():
    print("\n=== Customer Management System ===")
    print("Loading customer database...")
    
    while True:
        choice = main_menu()
        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        elif choice == 5:
            print("\nThank you for using the system. Goodbye!")
            break

if __name__ == "__main__":
    main()