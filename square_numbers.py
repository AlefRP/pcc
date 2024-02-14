squares = []

# Squares each value of 1 to 10
for value in range(1,11):
    square = value ** 2
    squares.append(square)
    
squares = []

# More concise
for value in range(1,11):
    squares.append(value ** 2)

print(squares)