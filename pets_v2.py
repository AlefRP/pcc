pets = ['cat', 'dog', 'cat', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

# This will remove all cats from the list
while 'cat' in pets:
    pets.remove('cat')

print(pets)