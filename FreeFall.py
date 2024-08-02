# This program will determine how quickly an object is travelling when it hits the ground

# Prompt the user to enter the height from which the object dropped in meters
distance = float(input("Enter the height from which the object is dropped in meters: "))

# Constants
acceleration = 9.8
initialVelocity = 0

# Computation for the final velocity
import math
finalVelocity = float(math.sqrt((initialVelocity**2) + (2 * acceleration * distance)))

# Display the output
print("The final velocity is: ", "{:,.2f}".format(finalVelocity), "m/s")


