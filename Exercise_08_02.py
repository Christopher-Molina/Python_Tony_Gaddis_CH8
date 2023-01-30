# Starting Out With Python 5th Edition: Chapter 8 - Exercise 2


def main():
    # Prompt user to enter a number as a string
    numbers = input('Enter a series of numbers with nothing separating them: ')

    # Initialize accumulator variable
    total = 0

    # For each number in numbers, add number to total
    for number in numbers:
        total += int(number)

    print(total)  # Display total


# Call the main function
if __name__ == '__main__':
    main()
