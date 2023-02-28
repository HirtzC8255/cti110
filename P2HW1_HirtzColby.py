# Calculator for Travel Expenses
# 2/28/23
# CTI-110 P2HW1 - Travel
# Colby Hirtz
#

print("This program calculates and displays travel expenses.\n")
budget = float(input("Enter Budget: "))
travel_des = str(input("\nEnter your travel destination: "))
gas = float(input("\nHow much do you think you will spend on gas? "))
hotel = float(input("\nApproximately, how much do you think you will need for accomodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))

print("\n------------Travel Expenses------------")
print("Location:           ", travel_des)
print("Initial Budget:      $" + str(budget))
print("Fuel:                $" + str(gas))
print("Accomodation:        $" + str(hotel))
print("Food:                $" + str(food), "\n----------------------------------------")
print("\nRemaining Balance:   $" + str(budget - (gas + hotel + food)))
