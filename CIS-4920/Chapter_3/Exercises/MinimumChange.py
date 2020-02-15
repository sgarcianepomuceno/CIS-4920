'''This program will provide the user the minimum change needed for the amount the user inputed.'''

# User enters an amount to provide change.
change = eval(input("Enter an amount to provide the change: "))

# Separating dollars and cents.
totalCents = int(change * 100)
numOfDollars = totalCents // 100
totalCents =  totalCents % 100

# Getting quarters.
numOfQuarters = totalCents // 25
totalCents = totalCents % 25

# Getting dimes.
numOfDimes = totalCents // 10
totalCents = totalCents % 10

# Getting nickels.
numOfNickels = totalCents // 5
totalCents = totalCents % 5

# Getting pennies.
numOfPennies = totalCents

print("Your amount", str(change), "consists of: ")
print('\t', numOfDollars, "dollar(s)")
print('\t', numOfQuarters, "quarter(s)")
print('\t', numOfDimes, "dime(s)")
print('\t', numOfNickels, "nickel(s)")
print('\t', numOfPennies, "penny(ies)")