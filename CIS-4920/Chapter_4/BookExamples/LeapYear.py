year = eval(input("Enter a year: "))

# Check if the year is a leap year
isLeapYear = (year % 4 == 0 and year % 100 != 0) or \
    (year % 400 == 0)

print(year, "is a leap year?", isLeapYear)