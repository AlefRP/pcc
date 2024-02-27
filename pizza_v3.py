# Using asterisk (*) in function definition tells python to create a tuple of arguments
# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested."""
#     print(toppings)

# def make_pizza(*toppings):
#     """Sintethize a pizza with requested toppings."""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(size, *toppings): # *args is a convention used, but you can use any name
    """Sintethize a pizza with requested toppings."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
        
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')