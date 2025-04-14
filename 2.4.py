def main():
    books = []
    
    print("Please enter 10 book titles:")
    
    while len(books) < 10:
        title = input(f"Enter book title #{len(books) + 1}: ").strip()
        
        if title:
            books.append(title.title())
        else:
            print("Title cant be empty.")
    
    books_sorted = sorted(books)
    
    print("\nYour books in alphabetical order:")
    for book in books_sorted:
        print(book)

if __name__ == "__main__":
    main()