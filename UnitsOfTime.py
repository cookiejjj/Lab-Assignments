# Displays the equivalent amount of time 

# Prompt the user to enter the number of seconds
secs = int(input("Enter the number of seconds: "))

# Constants
secondsPerMinute = 60
secondsPerHour = 3600
secondsPerDay = 86400

# Calculation for days
day = secs / secondsPerDay
secs = secs % secondsPerDay

# Calculation for hours
hrs = secs / secondsPerHour
secs = secs % secondsPerHour

# Calculation for minutes
mins = secs / secondsPerMinute
secs = secs % secondsPerMinute

# Display the output
print("The equivalent amount of time in the form D:HH:MM:SS is %d:%02d:%02d:%02d" % (day, hrs, mins, secs))
