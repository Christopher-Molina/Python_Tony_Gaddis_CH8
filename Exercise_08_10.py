# Starting Out With Python 5th Edition: Chapter 8 - Exercise 10


def main():
    # Prompt user for a string
    string = input('Write or paste text here: ')

    # Calculate most frequent character
    frequent = get_frequent(string)

    # Display most frequent character
    print('Most frequent character:', frequent)


# Function calculates the most frequent character in a string
def get_frequent(string):
    # Assume the first character is the most frequent
    frequent = string[0]

    # Initialize count
    count = 0
    for character in string:
        if string.count(character) > count:
            frequent = string[string.index(character)]
            count = string.count(character)
    return frequent


# Call the main function
if __name__ == '__main__':
    main()
