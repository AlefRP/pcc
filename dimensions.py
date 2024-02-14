# Tuples cannot change
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimension[0] = 250 # Will raise error, tuple is immutable

my_t = (3,) # tuple with one element

# Print all values of a tuple
for dimension in dimensions:
    print(dimension)
    
# Even being not possible change a tuple, I can put another value as a new tuple in a variable that holds a tuple
print("Original dimensions:")
print(dimensions)
dimensions = (400, 100)
print("\nModified dimensions:")
print(dimensions)