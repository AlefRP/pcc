# Count from 1 to 20
for number in range(1, 21):
    print(number)
    
million = list(range(1, 1000001))
print(min(million))
print(max(million))
print(sum(million))

# Odd numbers list
odd_numbers = list(range(1, 21, 2))

# Print each odd number
for number in odd_numbers:
    print(number)
    
multiplos_de_3 = list(range(3, 31, 3))
# multiplos_de_3 = [number for number in range(3, 31) if number % 3 == 0]

for number in multiplos_de_3:
    print(number)
    
cubos = []
for number in range(1, 11):
    cubo = number ** 3
    cubos.append(cubo)
    
print(cubos)

# Cubos usando list comprehension
cubos = [number ** 3 for number in range(1, 11)]
print(cubos)