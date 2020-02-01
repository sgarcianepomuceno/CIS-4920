'''This program will convert the amount of seconds
entered from the user to hours, minutes, and seconds.'''

# User enters seconds to convert.
totalSeconds = eval(input("Enter the seconds: "))

# Computes seconds into minutes.
totalMinutes = totalSeconds // 60

# Computes remaining seconds from minutes.
remainingSeconds = totalSeconds % 60

# Computes minutes into hours.
totalHours = totalMinutes // 60

# Computes remaining minutes from hours.
remainingMinutes = totalMinutes % 60

# Display result.
print(totalHours, "hour(s) and", remainingMinutes, "minute(s) and", remainingSeconds, "second(s).")