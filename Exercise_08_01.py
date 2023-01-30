# Starting Out With Python 5th Edition: Chapter 8 - Exercise 1


def main():
    # Input first name, middle name, and last name
    name = input('Enter your full name: ')

    # Split the string
    tokens = name.split()

    # Display initials with a dot
    print('Initials: ', end='')
    [print(ch[0].upper() + '.', end=' ') for ch in tokens]


# Call the main function
if __name__ == '__main__':
    main()