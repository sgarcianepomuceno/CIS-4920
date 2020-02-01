'''This program allows the user to enter the number
of integers they want shown after the tax amount.''' 

# The user enters the total price, tax, and number of integers after the decimal point. 
purchaseAmount = eval(input("Enter the price amount: "))
salesTax = eval(input("Enter the sales tax: ")) / 100
numberOfIntegers = eval(input("Enter the number of integers you want shown after the decimal point: "))

# The tax amount and the number of integers are computed.
taxAmount = int(purchaseAmount * salesTax * 10 ** numberOfIntegers) / 10 ** numberOfIntegers

# Display result.
print("The total price with", numberOfIntegers, "integers after the decimal point is $", taxAmount, ".")