# Calculator for Travel Expenses
# 2/9/2023
# CTI-110 P1HW2 - Travel Expense
# Colby Hirtz
#

print("This program calculates and displays travel expenses.\n")
budget = int(input("Enter Budget: "))
travel_des = str(input("\nEnter your travel destination: "))
gas = int(input("\nHow much do you think you will spend on gas? "))
hotel = int(input("\nApproximately, how much do you think you will need for accomodation/hotel? "))
food = int(input("\nLast, how much do you need for food? "))

print("\n------------Travel Expenses------------")
print("Location:", travel_des)
print("Initial Budget:", budget, "\n")
print("Fuel:", gas)
print("Accomodation:", hotel)
print("Food:", food, "\n")
print("Remaining Balance:", (budget - (gas + hotel + food)))
