# Starting Out With Python 5th Edition: Chapter 8 - Exercise 14 Part 3


def main():
    try:
        # Get datatable for gas prices
        gas_prices = process_file()

        # Calculate the highest price and the lowest price
        highest_prices, lowest_prices = get_prices(gas_prices)

        # Display the results
        display_results(highest_prices, lowest_prices)
    except (IOError, TypeError, ValueError, IndexError, Exception) as e:
        print(e)


# Function converts text file into a datatable
def process_file():
    # Open file for reading
    infile = open('GasPrices.txt', 'r')

    # Strip the newline character from the file and create a datatable
    datatable = []
    for line in infile:
        line = line.rstrip('\n')
        date, price = line.split(':')
        month, day, year = date.split('-')
        datatable.append([int(month), int(day), int(year), float(price)])

    # Close the file
    infile.close()

    return datatable


# Function returns the highest and lowest prices yearly
def get_prices(gas_prices):
    # Initialize empty lists
    highest_prices, lowest_prices = [], []

    # Initialize test variables
    current_year = gas_prices[0][2]
    max_element = min_element = gas_prices[0][3]
    max_date = min_date = ''

    for index in range(1, len(gas_prices)):
        if current_year != gas_prices[index][2]:
            highest_prices.append(max_date), lowest_prices.append(min_date)
            # Re-initialize variables
            current_year = gas_prices[index][2]
            max_element = min_element = gas_prices[index][3]
            max_date = min_date = gas_prices[index][:]
        else:
            # Find max and min elements with their dates
            if gas_prices[index][3] >= max_element:
                max_element = gas_prices[index][3]
                max_date = gas_prices[index][:]
            if gas_prices[index][3] <= min_element:
                min_element = gas_prices[index][3]
                min_date = gas_prices[index][:]
    highest_prices.append(max_date), lowest_prices.append(min_date)

    return highest_prices, lowest_prices


# Function displays the results formatted
def display_results(hp, lp):
    print('Highest Prices Yearly:')
    [print(f'{hp[index][0]}-{hp[index][1]}-{hp[index][2]}: {hp[index][3]}') for index in range(len(hp))]
    print('\nLowest Prices Yearly:')
    [print(f'{lp[index][0]}-{lp[index][1]}-{lp[index][2]}: {lp[index][3]}') for index in range(len(lp))]


# Call the main function
if __name__ == '__main__':
    main()
