# def describe_pet(animal_type, pet_name):
#     """Show information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
    
# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

# I can have strange results if i use different order
# describe_pet('harry', 'hamster')

# I can solve it using keyword arguments
# describe_pet(pet_name='harry', animal_type='hamster') # Change the order does not afect the result

# Defing a default value for a parameter
# def describe_pet(pet_name, animal_type='dog'): # But the first parameter must be the one without default value
#     """Show information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")


# describe_pet(pet_name='willie') # So animal type will be not necessary if it is a dog

# # To call for a animal different than dog
# describe_pet(pet_name='harry', animal_type='hamster')

# A dog named Willie
# describe_pet('willie')
# describe_pet(pet_name='willie')

# A hamster named Harry
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')

def describe_pet(animal_type, pet_name):
    """Show information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
 
# Without arguments - gets error   
# describe_pet()

# More arguments than parameters specified at the function definition
# describe_pet('willie', 'hamster', 'lucy')