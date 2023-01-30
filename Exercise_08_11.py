# Starting Out With Python 5th Edition: Chapter 8 - Exercise 11


def main():
    try:
        # Prompt user for a string
        string = input('Write or paste text here: ')

        # Tokenize the string using an uppercase letter as its delimiter
        tokens = tokenize(string)

        # Reconstruct the string to where only the first letter starts with an uppercase
        reconstructed = reconstruct(tokens)

        # Display the reconstructed string
        print(reconstructed)
    except (ValueError, TypeError, IndexError) as e:
        print(e)


# Function tokenizes the string using uppercase as a delimiter
def tokenize(string):
    # Initialize empty string
    reconstructed = ''
    for character in string:
        if character.isupper():
            reconstructed += '*' + character
        else:
            reconstructed += character

    # Tokenize using * as the delimiter and remove empty string in the list
    tokens = reconstructed.split('*')
    if tokens[0] == '':
        tokens.remove('')

    # Return the tokenized string
    return tokens


# Function returns the reconstructed string
def reconstruct(tokens):
    # Initialize the reconstructed string with the first index
    # since we will not lowercase string
    reconstructed = tokens[0] + ' '
    for index in tokens[1:]:
        for character in index:
            if character.isupper():
                reconstructed += character.lower() + index[1:] + ' '

    # Return the reconstructed string
    return reconstructed


# Call the main function
if __name__ == '__main__':
    main()
