# Prompt the user to enter the needed details
name = str(input("Enter your name: "))
birthYear = int(input("Enter the year you were born: "))
biologicalSex = str(input("Enter your sex (M or F): "))
collegeMajor = str(input("Enter your major: "))
currentGPA = float(input("Enter your current GPA: "))
a = int(input("Enter how many A(s) you earned this semester: "))
b = int(input("Enter how many B(s) you earned this semester: "))
c = int(input("Enter how many C(s) you earned this semester: "))
d = int(input("Enter how many D(s) you earned this semester: "))
f = int(input("Enter how many E(s) you earned this semester: "))

# Assign the indicated points for A, B, C, D, and F
aPoints = 4
bPoints = 3
cPoints = 2
dPoints = 1
fPoints = 0

# Computation for age
from datetime import datetime
currentYear = datetime.now().year
age = int(currentYear - birthYear)

# Computation for grades earned in semester
aEarned = int(a * aPoints)
bEarned = int(b * bPoints)
cEarned = int(c * cPoints)
dEarned = int(d * dPoints)
fEarned = int(f * fPoints)

# Computation for the total number of courses in the semester
totalNumber = int((a + b + c + d + f))

# Computation for Semester GPA
semesterGPA = round(((aEarned + bEarned + cEarned + dEarned + fEarned) / totalNumber), 1)

# Computation for Overall GPA
overallGPA = round(((semesterGPA + currentGPA) / 2), 1)
print()

# Display and format the Output
print("-" * 45)
print(f'{"Name:":21} {name}')
print(f'{"Sex:":21} {biologicalSex}')
print(f'{"Age:":21} {age}')
print(f'{"Major:":21} {collegeMajor}')
print(f'{"Overall GPA:":21} {overallGPA}')
print(f'{"Semester GPA:":21} {semesterGPA}')
print("-" * 45)
