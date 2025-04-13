import random

def main():
    print("Guess the number (1-100)")
    secret = random.randint(1, 100)
    
    while True:
        guess = int(input("Your guess: "))
        diff = abs(guess - secret)
        
        if diff == 0:
            print("Correct!")
            break
        elif diff <= 5:
            print("Very Hot")
        elif diff <= 15:
            print("Hot")
        elif diff <= 25:
            print("Cool")
        else:
            print("Cold")

if __name__ == "__main__":
    main()