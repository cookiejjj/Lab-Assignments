# Program that accepts three numbers and determine the highest and the lowest numbers. Also, displays the sum of the lowest and highest number

while True: # This program will continue to loop as long as the conditions are satisfied
    # Prompt the user to enter 3 numbers
    num1 = int(input("Enter the first number: ")) # first number
    num2 = int(input("Enter the second number: ")) # second number
    num3 = int(input("Enter the third number: ")) # third number

    # Determining the highest and lowest
    highest = max(num1, num2, num3) # max function returns the highest value among the three variables
    lowest = min(num1, num2, num3) # min function returns the lowest value among the three variables
    sum_high_low = highest + lowest # sum of the highest and lowest number
    print(f"Lowest: {lowest} \nHighest: {highest} \nSum: {sum_high_low}") # displays the output

    try_again = input("Do you want to try again?: (y/n) ") # asks the user if s/he wants to try again
    if try_again == "y" or try_again == "Y": # if yes, the program will restart
        continue
    elif try_again == "n" or try_again == "N": # if no, the program will end
        print("The program ends.")
        break
    else: # if invalid input, the program will also end since the user must type y to continue
        print("Invalid input. The program ends.")
        break

