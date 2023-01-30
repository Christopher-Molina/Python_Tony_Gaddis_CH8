# Starting Out With Python 5th Edition: Chapter 8 - Exercise 14 Part 1

def main():
    try:
        # Open file for reading
        infile = open('GasPrices.txt', 'r')

        # Calculate yearly averages
        yearly_averages = get_yearly_averages(infile)

        # Close the file
        infile.close()

        # Display results
        display_yearly_averages(yearly_averages)
    except (NameError, OSError, TypeError, ZeroDivisionError) as e:
        print(e)


# Function returns the yearly averages
def get_yearly_averages(gas_prices):
    current_year = ''  # Priming read for year
    weeks = total = 0  # Initialize accumulator variables
    yearly_averages = []  # Initialize empty list

    for index in gas_prices:
        # Strip the newline character
        index = index.rstrip('\n')

        # Separate date and price
        date, price = map(str, index.split(':'))
        month, day, year = map(str, date.split('-'))

        weeks += 1  # Increment weeks
        if current_year == '':
            current_year = year
            total += float(price)
        elif current_year != year:
            yearly_averages.append([current_year, round(total/(weeks-1), 3)])
            current_year = year
            weeks = 1
            total = float(price)
        else:
            total += float(price)

    yearly_averages.append([current_year, round(total / weeks, 3)])  # Append last year

    return yearly_averages  # Return list


# Function displays the yearly averages formatted
def display_yearly_averages(yearly_averages):
    print('Year\tAverage')  # Display header
    [print(f'{yearly_averages[index][0]}\t${yearly_averages[index][1]}') for index in range(len(yearly_averages))]


# Call the main function
if __name__ == '__main__':
    main()
