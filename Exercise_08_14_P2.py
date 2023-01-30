# Starting Out With Python 5th Edition: Chapter 8 - Exercise 14 Part 2


def main():
    try:
        # Open file for reading
        infile = open('GasPrices.txt', 'r')
        try:
            # Calculate monthly averages
            monthly_averages = get_monthly_averages(infile)

            # Display monthly averages
            display_monthly_averages(monthly_averages)
        except (TypeError, NameError, ValueError) as e:
            print(e)
        finally:
            infile.close()
    except OSError:
        print('ERROR: Can\'t open/read file')


# Function gets monthly averages in a list
def get_monthly_averages(gas_prices):
    current_month = ''  # Priming read for month
    weeks = total = 0  # Initialize accumulator variables
    monthly_averages = []  # Initialize empty list

    for line in gas_prices:
        # Strip the newline character from the file
        line = line.rstrip('\n')

        # Separate date and price
        date, price = map(str, line.split(':'))
        month, day, year = map(str, date.split('-'))

        weeks += 1  # Increment weeks
        if current_month == '':
            current_month = month
            total += float(price)
        elif current_month != month:
            # Append results to monthly averages
            monthly_averages.append([current_month, round(total / (weeks-1), 3)])

            # Re-initialize variables
            current_month = month
            total = float(price)
            weeks = 1
        else:
            total += float(price)
    monthly_averages.append([current_month, round(total / (weeks-1), 3)])

    return monthly_averages


# Function displays monthly averages
def display_monthly_averages(monthly_averages):
    current_year = 1993  # Set start year to 1993

    print(f'{current_year} Monthly Averages:')  # Display header
    for index in range(len(monthly_averages)):
        month = get_month_name(monthly_averages[index][0])
        if month == 'January':
            current_year += 1
            print(f'\n{current_year} Monthly Averages:')
            print(f'{get_month_name(monthly_averages[index][0])} - ${monthly_averages[index][1]}')
        else:
            print(f'{get_month_name(monthly_averages[index][0])} - ${monthly_averages[index][1]}')


# Function returns a month name
def get_month_name(month):
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
              7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    return months[int(month)]


# Call the main function
if __name__ == '__main__':
    main()
