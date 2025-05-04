def two_letter_combinations(characters):
    for first_char in characters:
        for second_char in characters:
            yield first_char + second_char

def main():
    letters = ['a', 'b', 'c', 'd', 'e']
    
    print(f"Generating all two-letter combinations from: {letters}")
    print("All combinations:")
    
    for combo in two_letter_combinations(letters):
        print(combo, end=' ')

if __name__ == "__main__":
    main()