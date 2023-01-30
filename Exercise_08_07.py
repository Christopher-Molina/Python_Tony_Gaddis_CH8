# Starting Out With Python 5th Edition: Chapter 8 - Exercise 7


def main():
    try:
        # Open file for reading
        infile = open('text.txt', 'r')

        # Read file into a list
        lines = infile.readlines()

        # Close the file
        infile.close()

        # Initialize accumulator variables
        uppercase = lowercase = digits = whitespace = 0
        for index in lines:
            for character in index:
                if character.isupper():
                    uppercase += 1
                elif character.islower():
                    lowercase += 1
                elif character.isdigit():
                    digits += 1
                elif character.isspace():
                    whitespace += 1

        # Display results
        print(f'Uppercase: {uppercase}\nLowercase: {lowercase}\nDigits: {digits}\nWhitespace: {whitespace}')
    except (IOError, IndexError, TypeError, ValueError) as e:
        print(e)


# Call the main function
if __name__ == '__main__':
    main()
