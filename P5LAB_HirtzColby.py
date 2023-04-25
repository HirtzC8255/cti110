# Define your function here.
def days_in_feb(user_year):
    days = 28
    if user_year % 4 == 0:
        if user_year % 100 == 0:
            if user_year % 400 == 0:
                days = 29
        else:
            days = 29
    return days

if __name__ == '__main__':
    year = int(input(''))
    days = days_in_feb(year)
    print(year, 'has', days, 'days in February.')