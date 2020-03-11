
print("Pattern A\n")
for row in range(1, 7):
    for column in range(1, row + 1):
        print(column, end = ' ')
    print()
    
print("\nPattern B\n")
for row in range(1, 7):
    for column in range(1, 8 - row):
        print(column, end = ' ')
    print()

print("\nPattern C\n")
