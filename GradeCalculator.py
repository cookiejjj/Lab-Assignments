# Program that will compute for the students average grade and displays the status of the student

# Prompt the user to input the needed details
name = str(input("Enter your Name: ")) # Name of the user
math = float(input("Enter your grade in Math: ")) # Grade in math of the user
science = float(input("Enter your grade in Science: ")) # Grade in science of the user
english = float(input("Enter your grade in English: ")) # Grade in english of the user

# Computation for the average grade
average_grade = round(((math + science + english) / 3), 2) # Add all the grades for each subject then divide to the number of subjects and round to 2 decimals
print(f"Average Grade: {average_grade}") # Display the average

# If the average grade, grade in math, science, and english is greater than or equal to 75
if average_grade >= 75 and math >= 75 and science >= 75 and english >= 75:
    print("Congratulations! \n You passed the semester.") # It will display that the user passed the semeseter

# However, if the average grade is greater than or equal to 75
elif average_grade >= 75:
    print("Congratulations!  \nYou passed the semester, \nbut you need to retake the following subjects(s): ") # It will display that the user passed but need to retake
    if math < 75: # But the grade in math is less than 75
        print("Math") # The user needs to retake in Math
    if science < 75:  # But the grade in science is less than 75
        print("Science") # The user needs to retake in Science
    if english < 75:  # But the grade in english is less than 75
        print("English") # The user needs to retake in English

# If the average grade, grade in math, science, and english is less than 75
else:
    print("You failed the semester.") # The user failed the semester
