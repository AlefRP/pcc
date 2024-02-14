my_foods = ['pizza', 'falafel', 'carrot cake']

# Copying the list
# friends_foods = my_foods[:]

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friends_foods)

# my_foods.append('cannoli')
# friends_foods.append('ice cream')

# print(my_foods)
# print(friends_foods)


# Esse método associa, não copia
friends_foods = my_foods

my_foods.append('cannoli')
friends_foods.append('ice cream')

# As duas adições aparecerão em ambas as listas
print(my_foods)
print(friends_foods)

print("Os três primeiros itens da minha lista de comidas favoritas são:")
for food in my_foods[(len(my_foods)-3):]:
    print(food)

print("\nOs três itens do meio da minha lista de comidas favoritas são:")
for food in my_foods[0:3]:
    print(food)
    
print("\nOs três últimos itens da minha lista de comidas favoritas são:")
for food in my_foods[-3:]:
    print(food)