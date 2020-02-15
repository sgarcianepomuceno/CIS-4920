# User enters all variables to create payroll statement.
name = input("Enter employee's name: ")
hours = eval(input("Enter number of hours worked in a week: "))
rate = eval(input("Enter hourly pay rate: "))
federalTax = eval(input("Enter federal tax withholding rate: "))
stateTax = eval(input("Enter state tax withholding rate: "))

# Printing payroll.
print("\n Employee Name:", name)
print('\t', "Hours Worked:", float(hours))
print('\t', "Pay Rate: " + '$' + str(rate))
print('\t', "Gross Pay: " + '$' + str(hours * rate))
print('\t', "Deductions:")
print('\t', "Federal Withholding (" + str(federalTax) + "):", federalTax)
print('\t', stateTax)