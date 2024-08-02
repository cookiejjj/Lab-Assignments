# Program using ladderized-if statement to display student's remarks based on the average grade
print("Average Grade Remarks") # Display Statement
average_grade = int(input("Enter average grade: ")) # Prompt the user to input his/her average grade
if 95 <= average_grade <= 100: # 95 - 100 Excellent
    print("Excellent")
elif 90 <= average_grade <= 94: # 90 - 94 Outstanding
    print("Outstanding")
elif 85 <= average_grade <= 89: # 85 - 89  Very Good
    print("Very Good")
elif 80 <= average_grade <= 84: # 80 - 84 Poor
    print("Good")
elif 75 <= average_grade <= 79: # 75 - 79 Good
    print("Poor")
elif 0 <= average_grade <= 74: # 0 - 74 Failed
    print("Failed")
else: # Input number is out of range (0 - 100)
    print("Grade out of range")
