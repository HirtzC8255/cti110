# CTI-110
# P2HW2 - List
# Colby Hirtz
# 2/28/23
#

num_list = []
mod1 = float(input("Enter grade for Module 1: "))
num_list.append(mod1)
mod2 = float(input("Enter grade for Module 2: "))
num_list.append(mod2)
mod3 = float(input("Enter grade for Module 3: "))
num_list.append(mod3)
mod4 = float(input("Enter grade for Module 4: "))
num_list.append(mod4)
mod5 = float(input("Enter grade for Module 5: "))
num_list.append(mod5)
mod6 = float(input("Enter grade for Module 6: "))
num_list.append(mod6)

lowest = min(num_list)
highest = max(num_list)
total = sum(num_list)
length = len(num_list)
average = round((total/length), 2)

print("\n------------Results------------")
print("Lowest Grade:        ", lowest)
print("Highest Grade:       ", highest)
print("Sum of Grades:       ", total)
print("Average:             ", average)
print("-------------------------------")
