def main():
    example_string = "Hello, Python programmers!"
    
    print("Iterating through the string:")
    for char in example_string:
        print(char, end=' ')
    print() 
    
    print("\nCharacter with the minimum ASCII value:")
    min_char = min(example_string)
    print(f"'{min_char}' (ASCII value: {ord(min_char)})")
    
    print("\nCharacter with the maximum ASCII value:")
    max_char = max(example_string)
    print(f"'{max_char}' (ASCII value: {ord(max_char)})")
    
    print("\nIndex of 'o':")
    index_o = example_string.index('o')
    print(index_o)
    
    print("\nConverting string to a list of characters:")
    char_list = list(example_string)
    print(char_list)
    
    print("\nCount of 'o' in the string:")
    count_o = example_string.count('o')
    print(count_o)

if __name__ == "__main__":
    main()