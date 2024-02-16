# Sorting a list permanently with the sort() method.
cars = ['bmw', 'audi', 'toyota', 'subaru']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Comparing values    
print(cars[0] == 'bmw')
car = 'audi'
print(car == 'bmw')

# Letras maisculas e minisculas diferem
car = 'Audi'
print(car == 'audi') # False
print(car.lower() == 'audi') # True

# cars.sort()
# print(cars)

# # Sorting Descending
# cars.sort(reverse=True)
# print(cars)

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print("Here is the original list:")
# print(cars)

# # Sorting the list temporarily with the sorted() function.
# print("\nHere is the sorted list:")
# print(sorted(cars))

# print("\nHere is the original list again:")
# print(cars)

# # Sorting a list in Reverse Order - last to first
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars)
# cars.reverse()
# print(cars)

# # Getting list length
# print(len(cars))