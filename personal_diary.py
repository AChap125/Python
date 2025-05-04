import os

def main():
    diary_folder = r'C:\Users\mrbig\Documents\add100\Python\4.1 4.2 and 4.3'
    diary_file = os.path.join(diary_folder, 'diary.txt')
    
    print("Welcome to your Diary")
    print(f"Entries will be saved to: {diary_file}\n")
    
    date = input("Enter today's date: ")
    time = input("Enter the current time: ")
    entry = input("Write your diary entry: ")
    
    try:
        os.makedirs(diary_folder, exist_ok=True)
        
        with open(diary_file, 'a') as f:
            f.write(f"Date: {date}\n")
            f.write(f"Time: {time}\n")
            f.write(f"Entry: {entry}\n\n")
        
        print("\nEntry saved!")
        
        print(f"\nFile saved to: {os.path.abspath(diary_file)}")
        print(f"File exists: {os.path.exists(diary_file)}")
        print(f"File size: {os.path.getsize(diary_file)} bytes")
        
    except Exception as e:
        print(f"\nError saving entry: {str(e)}")

if __name__ == "__main__":
    main()