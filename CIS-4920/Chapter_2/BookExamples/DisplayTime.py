'''This program allows the user to convert seconds to minutes'''

# User enters the amount of seconds to convert to time.
seconds = eval(input("Enter the amount of seconds to convert: "))

# Converts seconds to minutes.
minutes = seconds // 60

# Computes the remaining seconds.
remainder = seconds % 60 


print(seconds, "seconds is", minutes, "minute(s) and",
      remainder, "seconds.")