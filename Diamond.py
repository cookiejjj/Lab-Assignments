# Program that reads an integer and displays, using asterisks, a filled diamond of the given side length.
rows = int(input("Enter the number of side lengths: ")) # prompt the user to input the size

# top part of the diamond
for i in range(0, rows): # The range of the rows input by the user
    for j in range(i + 1, rows): # for the space of each row
        print(" ", end="")
    for j in range(i + 1): # for the first half (left) of asterisks in a row
        print("*", end="")
    for j in range(i): # for the second half (right) of asterisks in a row
        print("*", end="")
    print() # to move to next line

# bottom part of the diamond
# same as the top part of the diamond; only needs to subtract 1 for the row
for i in range(0, rows - 1):
    for j in range (i + 1): # for the space of each row
        print(" ", end="")
    for j in range(i, rows - 1): # for the first half (left) of asterisks in a row
        print("*", end="")
    for j in range(i+1, rows - 1): # for the second half (right) of asterisks in a row
        print("*", end="")
    print() # to move to next line
