# Starting Out With Python 5th Edition: Chapter 8 - Exercise 4


def main():
    try:
        # Initialize characters list
        characters = [' ', ',', '.', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                      'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        # Initialize morse code list
        morse = [' ', '--..--', '.-.-.-', '..--..', '-----', '.----', '..---', '...--', '....-', '.....',
                 '-....', '--...', '---..', '----.', '.-', '-...', '-.-.', '-..', '.', '..-.', '--.',
                 '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...',
                 '-', '..-', '...-', '.--', '-..-', '-.-', '--..']

        # Prompt user for input
        string = input('Enter a sentence to print in morse code: ').upper()

        # For every character in string, print its index in morse code
        for character in string:
            print(morse[characters.index(character)], end=' ')
    except (IndexError, ValueError, TypeError) as e:
        print(e)


# Call the main function
if __name__ == '__main__':
    main()
