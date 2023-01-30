# Starting Out With Python 5th Edition: Chapter 8 - Exercise 6


def main():
    try:
        # Open file for reading
        infile = open('text.txt', 'r')
        try:
            # Read the text file into a list
            text = infile.readlines()

            # Strip the newline from the list
            for line in range(len(text)):
                text[line] = text[line].rstrip('\n')

            # Initialize accumulator variable
            words = 0
            for index in text:
                for character in index:
                    if character == ' ':
                        words += 1
            words += 1  # Increment words after sentence

            # Display average words per sentence
            print(f'Average words per sentence is {words/len(text):.1f}')
        except (IndexError, TypeError, ValueError) as e:
            print(e)
        finally:
            # Close the file
            infile.close()
    except OSError:
        print('ERROR: Could not read/open file.')


# Call the main function
if __name__ == main():
    main()
