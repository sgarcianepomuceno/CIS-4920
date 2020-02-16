'''This program will display the future day of the week.'''

# User enters the day and number of days elapsed.
numDay = eval(input("Enter today's day (Sunday = 0, Saturday = 6): "))
daysPassed = eval(input("Enter the number of days elapsed since today: "))

# Assigning today's day.
if numDay == 0:
    today = "Sunday"
elif numDay == 1:
    today = "Monday"
elif numDay == 2:
    today = "Tuesday"
elif numDay == 3:
    today = "Wednesday"
elif numDay == 4:
    today = "Thursday"
elif numDay == 5:
    today = "Friday"
elif numDay == 6:
    today = "Saturday"

# Calculating and assigning the future day.
newDay = (numDay + daysPassed) % 7

if newDay == 0:
    newToday = "Sunday"
elif newDay == 1:
    newToday = "Monday"
elif newDay == 2:
    newToday = "Tuesday"
elif newDay == 3:
    newToday = "Wednesday"
elif newDay == 4:
    newToday = "Thursday"
elif newDay == 5:
    newToday = "Friday"
elif newDay == 6:
    newToday = "Saturday"    

# Display results.
print("Today is", today, "and the future day is", newToday)