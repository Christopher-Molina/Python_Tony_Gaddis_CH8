# Starting Out With Python 5th Edition: Chapter 8 - Exercise 12


def main():
    try:
        # Prompt user for a string
        sentence = input('Write or paste text here: ')

        # Convert to pig latin
        pig_latin = reconstruct(sentence)

        # Display reconstructed sentence in pig latin
        print(pig_latin)
    except IndexError:
        print(IndexError)
    except TypeError:
        print(TypeError)


# Function returns sentence in pig latin
def reconstruct(sentence):
    # Initialize vowels list
    vowels = ['A', 'E', 'I', 'O', 'U']

    # Tokenize the string
    tokens = sentence.split()

    # Initialize the reconstructed string
    reconstructed = ''
    for word in tokens:
        if word[0].upper() in vowels:
            reconstructed += word + 'ay '
        else:
            has_vowel = False
            for character in word:
                if character.upper() in vowels:
                    reconstructed += word[word.index(character):] + word[:word.index(character)] + 'ay '
                    has_vowel = True
                    break

            if has_vowel is False:
                reconstructed += word + 'ay '

    # Return the reconstructed string
    return reconstructed


# Call the main function
if __name__ == '__main__':
    main()
