'''This program allows the user to play Rock-Paper-Scissors'''

import random

# User enters chose.
user = eval(input("sciccor (0), rock (1), paper (2): "))

# Computer randomly chooses
computer = random.randint(0, 2)

# User winning scenarios.
if user == 0 and computer == 2:
    print("The computer is paper. You are scissor. You won.")
if user == 1 and computer == 0:
    print("The computer is scissor. You are rock. You won.")
if user == 2 and computer == 1:
    print("The computer is rock. You are paper. You won.")

# User losing scenarios.
if user == 0 and computer == 1:
    print("The computer is rock. You are scissor. You lose.")
if user == 1 and computer == 2:
    print("The computer is paper. You are rock. You lose.")
if user == 2 and computer == 0:
    print("The computer is scissor. You are paper. You lose.")

# User and computer draw.
if user == computer:
    if user == 0:
        print("The computer is scissor. You are scissor too. It is a draw.")
    elif user == 1:
        print("The computer is rock. You are rock too. It is a draw.")
    else:
        print("The computer is paper. You are paper too. It is a draw.")