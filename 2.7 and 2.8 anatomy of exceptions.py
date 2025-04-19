def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", 
                   "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    
    display_artists(top_artists)
    replace_artist(top_artists)
    display_artists(top_artists)
    replace_artist_combined(top_artists)
    display_artists(top_artists)

def display_artists(artists):
    for i, artist in enumerate(artists):
        print(f"{i}: {artist}")

def replace_artist(artists):
    try:
        index = int(input("Enter the index of the artist to replace: "))
        new_artist = input("Enter the new artist name: ")
        artists[index] = new_artist
    except ValueError:
        print("Error: Please enter a valid number for the index")
    except IndexError:
        print(f"Error: Index must be between 0 and {len(artists) - 1}")

def replace_artist_combined(artists):
    try:
        index = int(input("Enter the index of the artist to replace: "))
        new_artist = input("Enter the new artist name: ")
        artists[index] = new_artist
    except (ValueError, IndexError):
        print("An input error occurred.")

if __name__ == "__main__":
    main()