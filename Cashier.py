# Prompt the user to enter his/her name
firstName = str(input("What is your first name: "))
lastName = str(input("What is your last name: "))
print()

# Prompt the user to enter its item and its price
firstItem = str(input(firstName + ", what is your first item: "))
firstItemPrice = float(input("What is the price of " + firstItem + ": "))
secondItem = str(input(firstName + ", what is your second item: "))
secondItemPrice = float(input("What is the price of " + secondItem + ": "))
thirdItem = str(input(firstName + ", what is your third item: "))
thirdItemPrice = float(input("What is the price of " + thirdItem + ": "))
print()


# Prompt the user to input the sales tax percentage
salesTaxPercentage = float(input("What is the sales tax percent: "))
print()

# Compute the total amount of the items purchased
totalAmount = round(float(firstItemPrice + secondItemPrice + thirdItemPrice), 2)

# Compute for the sales tax amount
salesTaxValue = float(salesTaxPercentage / 100)
salestaxAmount = round(float(totalAmount * salesTaxValue), 2)

# Compute for the total amount with sales tax amount
totalAmountWithTax = round(float(totalAmount + salestaxAmount), 2)

# Display the total amount due and the money provided
print("The total amount due is $" + str(totalAmountWithTax))
moneyProvided = float(input(("Money you providing to pay the $" + str(totalAmountWithTax) + ":$")))
print()

# Compute for the change
change = round(float(moneyProvided - totalAmountWithTax), 2)

# Display the receipt
print("Printing the receipt.........")
print()

# Display and format the Output
print(f'{"Customer:":>20}       {firstName + " " + lastName}')
print(f'{firstItem + ":":>20}       {"$" + str(firstItemPrice)}')
print(f'{secondItem + ":":>20}       {"$" + str(secondItemPrice)}')
print(f'{thirdItem + ":":>20}       {"$" + str(thirdItemPrice)}')
print(f'{"Total Amount:":>20}       {"$" + str(totalAmount)}')
print(f'{"Sales Tax Amount:":>20}       {"$" + str(salestaxAmount)}')
print(f'{"Your total:":>20}       {"$" + str(totalAmountWithTax)}')
print(f'{"Money provided:":>20}       {"$" + "%.2f" % moneyProvided}')
print(f'{"Your change:":>20}       {"$" + str(change)}')
print()
print("Thank you, " + firstName + ", for shopping with us!")
