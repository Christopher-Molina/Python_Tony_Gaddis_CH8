# Starting Out With Python 5th Edition: Chapter 8 - Exercise 14 Part 4 and Part 5
from operator import itemgetter


def main():
    try:
        # Open file for reading
        infile = open('GasPrices.txt', 'r')

        # Sort the file from lowest to highest and highest to lowest
        sorted_list(infile)

        # Close the file
        infile.close()
    except (OSError, IndexError, TypeError, ValueError) as e:
        print(e)


# Function writes sorted lists to two text files
def sorted_list(infile):
    # Sort the dates from lowest to highest and highest to lowest
    lowest_to_highest = []
    highest_to_lowest = []

    # Strip the newline character and separate date and price
    for line in infile:
        line = line.rstrip('\n')
        date, price = line.split(':')
        lowest_to_highest.append([date, float(price)]), highest_to_lowest.append([date, float(price)])

    lowest_to_highest = sorted(lowest_to_highest, key=itemgetter(1))
    highest_to_lowest = sorted(highest_to_lowest, key=itemgetter(1), reverse=True)

    # Open file for writing
    outfile = open('lowest_highest.txt', 'w')
    write_data(lowest_to_highest, outfile)

    # Open file for writing
    outfile = open('highest_lowest.txt', 'w')
    write_data(highest_to_lowest, outfile)

    # Close the file
    outfile.close()
    print('Data Written to lowest_highest.txt\nData Written to highest_lowest.txt')


# Function writes data to a text file
def write_data(file, outfile):
    [outfile.write(f'{index}\n') for index in file]


# Call the main function
if __name__ == '__main__':
    main()
