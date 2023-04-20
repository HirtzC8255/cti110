# CTI-110
# P4HW2 - Salary
# Colby Hirtz
# 4/20/23
#

name = 'None'
overtime = 0
overtimePay = 0
regHourPay = 0
grossPay = 0
totalE = 0
totalO = 0
totalH = 0
totalG = 0

while name != 'Done':
    overtime = 0
    regHourPay = 0
    grossPay = 0
    name = input("\nEnter employee's name or" + ' "Done" ' + "to terminate: ")
    if name == "Done":
        print("\nTotal number of employees entered:", totalE)
        print("Total amount paid for overtime:", totalO)
        print("Total amount paid for regular hours:", totalH)
        print("Total amount paid in gross:", totalG)
    else:
        totalE += 1
        hours = float(input("How many hours did " + name + " work? "))
        pay = float(input("What is " + name + "'s pay rate? "))
        if hours > 40:
            overtime = hours - 40
            regHourPay = pay * 40
        else:
            regHourPay = pay * hours
        overtimePay = overtime * pay * 1.5
        grossPay = regHourPay + overtimePay
        totalO = totalO + overtimePay
        totalH = totalH + regHourPay
        totalG = totalG + grossPay
        print('\nEmployee name:    ', name)
        print('\nHours Worked   Pay Rate   OverTime   OverTime Pay      RegHour Pay        Gross Pay')
        print("---------------------------------------------------------------------------------------------")
        print(hours, "          "+ str(pay) +  "      ", str(overtime), "      ", str(overtimePay), "             $" + str(regHourPay), "            $" + str(grossPay))

