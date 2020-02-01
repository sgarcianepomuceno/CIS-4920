'''This program calculates the monthly payment of a loan when they provide
 the loan amount, APR, and the duration(in years) of the loan.'''   

# User enters the loan amount, APR, and number of years.
loanAmount = eval(input("Enter the loan mount: "))
monthlyAPR = (eval(input("Enter the APR: ")) / 12 / 100)
numberOfYears = eval(input("Enter the number of years of the loan: "))

# The monthly payment and the total payment is computed using user's input.
monthlyPayment = (loanAmount * monthlyAPR) / (1 - 1 / (1 + monthlyAPR)**(numberOfYears * 12))
totalPayment = monthlyPayment * numberOfYears * 12

# Display result.
print("Your monthly payment is $",
      int(monthlyPayment * 100) / 100)
print("Your total payment is $",
      int(totalPayment * 100) / 100)