# Starting Out With Python 5th Edition: Chapter 8 - Exercise 8


def main():
    # Prompt user for a string
    string = input('Write or paste text here: ')

    # Capitalize the string
    capitalize(string)


# Function capitalizes a sentence
def capitalize(string):
    # Replace multiple spaces with one space
    string = ' '.join(string.split())

    # Tokenize the string
    tokens = string.split('. ')

    reconstructed = ''
    for index in tokens:
        if index == tokens[len(tokens)-1]:
            reconstructed += index.replace(index, index[0].upper()) + index[1:]
        else:
            reconstructed += index.replace(index, index[0].upper()) + index[1:] + '. '
    print(reconstructed)


# Call the main function
if __name__ == '__main__':
    main()
