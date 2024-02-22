sandwich_orders = ['ham sandwich', 'egg sandwich', 'bacon sandwich', 'pastrami sandwich', 'pastrami sandwich', 'pastrami sandwich']
finished_sandwiches = []

# This removes pastrami sandwiches from the list of sandwich orders.
if 'pastrami sandwich' in sandwich_orders:
    print("Sorry, we are out of pastrami sandwich.")
    while 'pastrami sandwich' in sandwich_orders:
        sandwich_orders.remove('pastrami sandwich')

# Interate through the list of sandwich orders finishing each sandwich.
while sandwich_orders:
    
    # Remove the sandwich from the list of sandwich orders and add it to the list of finished sandwiches.
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + ".")
    finished_sandwiches.append(sandwich)

# Display each sandwich that was made.  
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} has been made.")