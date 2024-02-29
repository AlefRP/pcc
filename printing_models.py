def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design. 
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# # Begin with some unprinted designs: 
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# print_models(unprinted_designs[:], completed_models) # If I want to keep the original list, I need to pass a copy of the list to the function.
# show_completed_models(completed_models)


# # Simulate printing each design, until none are left. 
# # Move each design to completed_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()

#     # Simulate creating a 3D print from the design. 
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design) 


# # Display all completed models. 
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)