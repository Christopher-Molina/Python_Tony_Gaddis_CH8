# Starting Out With Python 5th Edition: Chapter 8 - Exercise 3


def main():
    # Input date in the format MM/DD/YY
    date = input('Enter a date in the format mm/dd/yyyy: ')

    # Tokenize the string
    tokens = tokenize(date)

    # Format the date
    format_date(tokens)


# Function returns the string tokenized
def tokenize(date):
    return date.split('/')


# Function formats the date
def format_date(tokens):
    month = get_month(int(tokens[0]))
    print(f'{month} {tokens[1]}, {tokens[2]}')


# Function returns the name of the month entered as an integer
def get_month(month):
    if month == 1:
        return 'January'
    elif month == 2:
        return 'February'
    elif month == 3:
        return 'March'
    elif month == 4:
        return 'April'
    elif month == 5:
        return 'May'
    elif month == 6:
        return 'June'
    elif month == 7:
        return 'July'
    elif month == 8:
        return 'August'
    elif month == 9:
        return 'September'
    elif month == 10:
        return 'October'
    elif month == 11:
        return 'November'
    elif month == 12:
        return 'December'
    else:
        return 'Invalid Month'


# Call the main function
if __name__ == '__main__':
    main()
