import os

def main():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'sales_totals.txt')
        
        print(f"Looking for file at: {file_path}")
        
        total = 0.0
        count = 0
        
        print("Sales Figures:")
        print("-------------")
        
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    amount = float(line.strip())
                    total += amount
                    count += 1
                    print(f"{amount:,.2f}")
                except ValueError:
                    print(f"Invalid data skipped: {line.strip()}")
        
        average = total / count if count > 0 else 0
        
        print("\nSummary:")
        print("--------")
        print(f"Total: {total:,.2f}")
        print(f"Number of entries: {count}")
        print(f"Average: {average:,.2f}")
    
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()