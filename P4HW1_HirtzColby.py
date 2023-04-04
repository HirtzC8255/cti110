# CTI-110
# P4HW1 - Score List
# Colby Hirtz
# 4/4/23
#

grade = 0
total = 0
grade_list = []

scores = int(input('How many scores do you want to enter? '))

for i in range(0, scores):
    grade = float(input('Enter score #' + str(i + 1) + ': '))
    while grade < 0 or grade > 100:
        print('INVALID Score entered!!!!')
        print('Score should be between 0 and 100')
        grade = int(input('Enter score #' + str(i + 1) + ' again: '))
    grade_list.append(grade)
lowest = min(grade_list)
grade_list.remove(lowest)
print('-------------Results-----------')
print('Lowest Score  :', lowest)
print('Modified List :', grade_list)
average = sum(grade_list) / i
print('Scores Average:', average)
if average >= 90:
    print('Grade         : A')
elif average >= 80 and average < 90:
    print('Grade         : B')
elif average >= 70 and average < 80:
    print('Grade         : C')
elif average >= 60 and average < 70:
    print('Grade         : D')
else:
    print('Grade         : F')
print('-------------------------------')
