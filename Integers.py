# Program that reads integers, finds the largest of them, count its occurrences, and input ends with number 0.
# Initialize the variables
max = None # stores the maximum number and is equal to none since there is no value yet
count = 0 # stores the number of occurrences that the maximum number is inputted and starts counting from 0

# This is the loop of the program
while True: # The program will continue to loop if it satisfies the condition
    number = int(input("Enter a number (0: for end of input): ")) # The input of the user will store in the "number" variable
    if number == 0: # If the number is equals to 0 (condition),
        break # The program will take a break and will not execute the next lines of conditions.

    elif number == max: # If the number is equals to the largest number
            count += 1 # There will be an increment in count by 1

    elif max is None or number > max:  # Checks the input if it is greater than the largest number input
            max = number # If it satisfies the above condition, then the max will be equal to the number
            count = 1 # It will store 1 to the count to start counting of the occurrences

if max is not None: # Checks the max if there is already an assigned value other than none
        print(f"The largest number is {max}") # It will display the output which is the largest number
        print(f"The occurrence count of the largest number is {count}.") # Displays the output of the number of occurrences of the largest number
else: # If it does not satisfy the condition above
        print("End of Program!") # It will print the statement. It will be output if the user entered 0 since there is no other assigned value for the max other than none.

