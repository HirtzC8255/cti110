# CTI-110
# P3HW2 - Salary
# Colby Hirtz
# 3/21/23
#

name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay = float(input("Enter employee's pay rate: "))
overtime = 0
overtimePay = 0
regHourPay = 0
grossPay = 0

if hours > 40:
    overtime = hours - 40
    regHourPay = pay * 40
else:
    regHourPay = pay * hours
overtimePay = overtime * pay
grossPay = regHourPay + overtimePay

print('----------------------------------')
print('Employee name:    ', name)
print('\nHours Worked   Pay Rate   OverTime   OverTime Pay      RegHour Pay        Gross Pay')
print("---------------------------------------------------------------------------------------------")
print(hours, "          "+ str(pay) +  "      ", str(overtime), "      ", str(overtimePay), "             $" + str(regHourPay), "            $" + str(grossPay))
