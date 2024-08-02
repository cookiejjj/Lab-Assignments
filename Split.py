# Program that reads first 2 values form the keyboard; a starting and an ending value.
# Also, sums all the even numbers between those values including endpoints and displays the sum.

# The program will continue to loop as long as it is true and satisfies the statements
while True:
    values = input("Enter starting and ending: ") # store two values in one variable
    start_number, end_number = map(int, values.split()) # separate two values using split and map to convert into integers

    if start_number > end_number: # if the ending number is less than the starting number
        total_sum = 0 # the sum is equal to 0

    elif start_number < end_number: # if the ending number is greater than, then it will execute the below statements
        # There is a loop again since the program needs to add all the even numbers inside the range
        total_sum = 0 # initialize the variable "total_sum"
        for num in range(start_number, end_number + 1):
            if num % 2 == 0: # condition to determine the even numbers inside the range
                total_sum += num # increment

    elif start_number == end_number: # if the starting number and ending number is the same
        if start_number % 2 == 0 or end_number % 2 == 0: # if even, it will result to same number
            total_sum = start_number
        elif start_number % 2 == 1 or end_number % 2 == 1: # if odd, it will result to 0
            total_sum = 0

    # Display the sum of even numbers
    print(f"Sum of evens = {total_sum}") # This is not indented since whether the input satisfies the first or second condition, it should display the output

    # Loop
    try_again = input("Do you want to try again?: (y/n) ")  # asks the user if s/he wants to try again
    if try_again == "y" or try_again == "Y":  # if yes, the program will restart
        continue
    elif try_again == "n" or try_again == "N":  # if no, the program will end
        print("The program ends.")
        break
    else:  # if invalid input, the program will also end since the user must type y to continue
        print("Invalid input. The program ends.")
        break


