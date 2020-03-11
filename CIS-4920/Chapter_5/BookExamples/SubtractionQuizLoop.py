import random
import time

correctCount = 0 #Count number of correct answers
count = 0 # Count the number of question
numberOfQuestions = 5 # Number of questions

startTime = time.time() # Get start time

while count < numberOfQuestions:
    # Generate two random numbers
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)
    
    # If number1 is less than number2
    if number1 < number2:
        number1, number2 = number2, number1
    
    # Prompt the user to answer the question.
    answer = eval(input("What is " + str(number1) + " - " + str(number2) + "? "))
    
    # Grade the answer and display the result
    if answer == number1 - number2:
        print("You are correct!")
        correctCount = correctCount + 1
    else:
        print("Your answer is wrong.\n", number1, "-", number2, "is", number1 - number2)
    # Increase the count
    count += 1

endTime = time.time() #Get end time
testTime = int(endTime - startTime) # Get test time
print("\nCorrect count is", correctCount, "out of",
      numberOfQuestions, "\nTest time is", testTime, "seconds.")