# Starting Out With Python 5th Edition: Chapter 8 - Exercise 9


def main():
    # Input a string
    string = input('Write or paste text here: ')

    # Count vowels and consonants
    vowels, consonants = get_vowels_consonants(string)

    # Display vowels and consonants
    print(f'Vowels: {vowels}\nConsonants: {consonants}')


# Function returns the number of vowels and consonants
def get_vowels_consonants(string):
    vowels = 0
    consonants = 0
    for character in string:
        if character.upper() in 'AEIOU':
            vowels += 1
        else:
            consonants += 1
    return vowels, consonants


# Call the main function
if __name__ == '__main__':
    main()
