# This program will compute the tax amount, tip amount, and total amount of a meal by entering the gross amount of the meal

# Prompt the user to input the cost of the meal
mealCost = float(input("Enter the cost of the meal you ordered at a restaurant: "))

# Local tax rate
valueAddedTax = 0.12

# Tip rate
tipRate = 0.20

# Computation for the tax, tip, and the total amount of the meal
mealTax = float(mealCost * valueAddedTax)
mealTip = float(mealCost * tipRate)
totalMealCost = float(mealCost + mealTip + mealTax)

# Display and formatting of the output
print("The tax amount is: $", "{:,.2f}".format(mealTax), sep='')
print("The tip amount is: $", "{:,.2f}".format(mealTip), sep='')
print("The grand total of the meal (with tax and tip) is: $", "{:,.2f}".format(totalMealCost), sep='')

