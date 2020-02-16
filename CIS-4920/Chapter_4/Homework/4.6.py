'''This program determines whether the user is underwight, normal, overweight, or obese.'''

# Prompt the user to enter weight in pounds
weight = eval(input("Enter weight in pounds: "))

# Prompt the user to enter height in feet and inches
feet = eval(input("Enter feet: "))
inches = eval(input("Enter inches: "))

KILOGRAMS_PER_POUND = 0.45359237
METER_PER_INCHE = 0.0254

height = 12 * feet + inches

#Compute BMI
weightInKilograms = weight * KILOGRAMS_PER_POUND
heightInMeters = height * METER_PER_INCHE
bmi = weightInKilograms / (heightInMeters * heightInMeters)

# Display result
print("BMI is", format(bmi, ".2f"))
if bmi < 18.5:
    print("Your are Underweight")
elif bmi < 25:
    print("Your are Normal")
elif bmi < 30:
    print("Your are Overweight")
else:
    print("Your are Obese")