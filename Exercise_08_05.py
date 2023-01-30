# Starting Out With Python 5th Edition: Chapter 8 - Exercise 5


def main():
    try:
        # Prompt user for an alphanumeric phone number
        number = input_validation()

        # Tokenize the string
        tokens = tokenize(number)

        # Display the numerical number
        display(tokens)
    except Exception as e:
        print(e)


# Function validates input from the user
def input_validation():
    # Prompt user for an alphanumeric phone number as a string
    string = input('Enter an alphanumeric number in the format XXX-XXX-XXXX: ')

    # Calculate length of string
    length = condition_one(string)

    # Calculate whether string contains invalid characters
    invalid_char = condition_two(string)

    # Calculate hyphen count
    hyphen_ct = condition_three(string)

    # Validate the input
    while (length != 12) or (invalid_char is True) or (hyphen_ct != 2)\
            or (string[3] != '-' and string[7] != '-'):
        string = input('ERROR: Invalid format, try again: ')
        length = condition_one(string)
        invalid_char = condition_two(string)
        hyphen_ct = condition_three(string)
    return string.upper()


# Function returns the length of a string
def condition_one(string):
    return len(string)


# Function determines whether the user input contains an invalid character
def condition_two(string):
    invalid_chars = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=',
                     '{', '}', '[', ']', ':', ';', '"', '\'', ',', '<', '>', '.', '?', '/']

    return any(item in list(string) for item in invalid_chars)


# Function calculates the number of times the hyphen character appears
def condition_three(string):
    return string.count('-')


# Function tokenizes the string
def tokenize(string):
    return string.split('-')


# Function displays the numeric number
def display(tokens):
    number = ''
    for index in tokens:
        for char in index:
            if char in 'ABC':
                number += '2'
            elif char in 'DEF':
                number += '3'
            elif char in 'GHI':
                number += '4'
            elif char in 'JKL':
                number += '5'
            elif char in 'MNO':
                number += '6'
            elif char in 'PQRS':
                number += '7'
            elif char in 'TUV':
                number += '8'
            elif char in 'WXYZ':
                number += '9'
            else:
                number += char
        if len(number) % 2 != 0:
            number += '-'
    print(number)


# Call the main function
if __name__ == '__main__':
    main()
