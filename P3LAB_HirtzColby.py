is_leap_year = False
   
input_year = int(input())

''' Type your code here. '''
if (input_year % 100 != 0) and (input_year % 4 == 0):
    is_leap_year = True

if (input_year % 100 != 0) and (input_year % 4 != 0):
    is_leap_year = False

if (input_year % 100 == 0) and (input_year % 400 == 0):
    is_leap_year = True

if (input_year % 100 == 0) and (input_year % 400 != 0):
    is_leap_year = False

if is_leap_year == True:
    print(input_year, "- leap year")

if is_leap_year == False:
    print(input_year, "- not a leap year")