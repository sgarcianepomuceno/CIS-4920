'''This program will allow user to enter information to create a payroll statement.'''

# User enters all variables to create payroll statement.
name = input("Enter employee's name: ")
hours = eval(input("Enter number of hours worked in a week: "))
rate = eval(input("Enter hourly pay rate: "))
federalTax = eval(input("Enter federal tax withholding rate: "))
stateTax = eval(input("Enter state tax withholding rate: "))

# Calculating certain information needed to enter the payroll.
grossPay = hours * rate
fedWith = grossPay * federalTax
stateWith = grossPay * stateTax
totalDeduction = fedWith + stateWith
netPay = grossPay - fedWith - stateWith

# Printing payroll.
print("\n Employee Name:", name)
print('\t', "Hours Worked:", float(hours))
print('\t', "Pay Rate: " + '$' + str(rate))
print('\t', "Gross Pay: " + '$' + str(grossPay))
print('\t', "Deductions:")
print('\t', '\t', "Federal Withholding (" + str(format(federalTax, "3.1%")) + "): $" + str(round(fedWith, 2)))
print('\t', '\t', "State Withholding (" + str(format(stateTax, "3.1%")) + "): $" + str(round(stateWith, 2)))
print('\t', '\t',"Total Deduction:", "$" + str(round(totalDeduction, 2)))
print('\t', "Net Pay:", "$" + str(round(netPay, 2)))