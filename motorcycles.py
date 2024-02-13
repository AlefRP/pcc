# Cahnging the value of an item in a list

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

# Adds an element to the beginning of the list, moves others to the right
motorcycles.insert(0, 'ducati')

# Delete an item from a list
del motorcycles[0]

# Remove the last item from a list, I can also save it in a variable cause pop returns the value removed
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

print(f"The last motorcycle I owned was a {popped_motorcycle.title()}")

# I also can remove from a specific index using pop
popped_motorcycle = motorcycles.pop(1)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# Remove item from list by value
motorcycles.remove('ducati')

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# I will remove using a varible value in remove method
# Remove just removes the first occurance of the value in the list
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f"\nA {too_expensive.title()} is too expensive for me.")