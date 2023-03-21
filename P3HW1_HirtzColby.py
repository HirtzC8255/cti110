# CTI-110
# P2HW2 - List
# Colby Hirtz
# 2/28/23
#


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

# determine letter grade for average

print("\n------------Results------------")
print("Lowest Grade:        ", round(low, 2))
print("Highest Grade:       ", round(high, 2))
print("Sum of Grades:       ", round(total, 2))
print("Average:             ", round(avg, 2))
print("-------------------------------")

if avg >= 90:
    print('Your grade is: A')
elif avg >= 80 and avg < 90:
    print('Your grade is: B')
elif avg >= 70 and avg < 80:
    print('Your grade is: C')
elif avg >= 60 and avg < 70:
    print('Your grade is: D')
else:
    print('Your grade is: F') # TO DO: finish this





