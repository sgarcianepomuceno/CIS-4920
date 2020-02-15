'''This program generates a random integer using
the time function to display an uppercase letter.'''

import time
import random

# Generate a random integer between 65 and 90 using time.time().
a = time.time()
b = (int(a * 100))
c = b % 100
d = random.randint(65,90)

# Display upper-case letter. 
if(c <= 64): 
    print(chr(d))
elif(c >= 91):
    print(chr(d))
else:
    print(chr(c))