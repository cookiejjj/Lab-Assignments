# This program will read for the number of containers and the compute for the amount of refund.

# Prompt the user to enter the number of containers
container = float(input("Enter the number of containers that holds one liter or less: "))

# Amount of deposit for each container that holds one liter or less
deposit = 2

# Computing for the amount of refund
refund = float(container * deposit)

# Display and format the output
print("Your total refund is: $", "{:,.2f}".format(refund), sep='')

