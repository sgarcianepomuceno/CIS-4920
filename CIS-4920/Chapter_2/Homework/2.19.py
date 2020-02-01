'''This program will calculate the future investment value.'''

# User inputs variables for TVM.
investmentAmount = eval(input("Enter investment amount: "))
APR = eval(input("Enter annual interest rate: "))
numberOfYears = eval(input("Enter number of years: "))

# Convert APR to monthly interest and years to months.
monthlyInterest = APR / 100 / 12
numberOfMonths = numberOfYears * 12

# Compute future investment value.
futureInvestmentValue = investmentAmount * (1 + monthlyInterest) ** numberOfMonths

# Display results.
print("Accumulated value is", int(futureInvestmentValue * 100) / 100)