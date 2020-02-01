'''This program will calculate the total
price of service and the gratuity.'''

# Declare variables.
subtotal, tip = eval(input("Enter the subtotal and a gratuity rate: "))

# Compute total and gratuity.
gratuity = subtotal * (tip / 100)
total = subtotal + gratuity

# Display result.
print("The gratuity is", int(gratuity * 100) / 100, 
      "and the total is", int(total * 100) / 100)