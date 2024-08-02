# Program that computes the perimeter of a polygon
# Reads the x and y values for the first point of a polygon

# Import math module since the formula includes square root
import math

# Read the first point:
# For x coordinate
x_previous_string = input("Enter x-coordinate of the first point: ") # Prompts the user to enter the x coordinate of the first point
if x_previous_string == "": # If the user does not enter an input
    print("There is no input entered. The program ends.")
    exit() # The program ends

# For y coordinate
y_previous_string = input("Enter y-coordinate of the first point: ")

# Check if the first point coordinates are numeric
if not (x_previous_string.isnumeric() and y_previous_string.isnumeric()): # If the inputs are not numeric then the program ends
    print("Invalid input for the first point. Please enter valid numerical coordinates.")
    exit()

# If the inputs are numeric, then it needs to be converted into float data type and stored in a new variable
x_prev_float = float(x_previous_string)
y_prev_float = float(y_previous_string)

# Initialize perimeter
perimeter_polygon = 0

# The conditions and statements inside the loop is the same logic in the above
# Reads the following points until a blank line is entered for x-coordinate
while True: # As long as the input satisfies the conditions, the loop will continue
    # For x coordinate
    x_coord_str = input("Enter x-coordinate (blank line to finish): ")
    if x_coord_str == "": # However, if the user entered nothing the loop will break and will only execute the following lines that is not inside the loop
        break

    # For y coordinate
    y_coord_str = input("Enter y-coordinate: ")

    # Check if the coordinates are numeric
    if not (x_coord_str.isnumeric() and y_coord_str.isnumeric()):
        print("Invalid input. Please enter valid numerical coordinates.")
        continue # The loop will continue it the coordinates are numeric

    # If the inputs are numeric, then it needs to be converted into float data type and stored in a new variable
    x = float(x_coord_str)
    y = float(y_coord_str)

    # Calculate the distance using the distance formula from point to point and add to the perimeter
    # distance = sqrt((x2 – x1)**2 + (y2 – y1)**2 ).
    perimeter_polygon += math.sqrt((x_prev_float - x)**2 + (y_prev_float - y)**2)

    x_prev_float, y_prev_float = x, y

# Add the distance and compute using the distance formula from point to point
perimeter_polygon += math.sqrt((x_prev_float - float(x_previous_string))**2 + (y_prev_float - float(y_previous_string))**2)

# Display the total perimeter
print(f"The perimeter of the polygon is: {perimeter_polygon:.2f}")
