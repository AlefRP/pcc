class Restaurant:
    def __init__(self, name, cuisine_type, number_served = 0):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
        
    def describe_restaurant(self):
        """
        A method to describe the restaurant, printing its name and cuisine type.
        """
        print(f"The restaurant name is {self.name} and the cuisine type is {self.cuisine_type}")
        
    def open_restaurant(self):
        """
        Open the restaurant and print a message with the restaurant's name.
        """
        print(f"{self.name} is now open!")
        
    def set_number_served(self, number_served):
        """
        Set the number of customers that have been served.
        """
        self.number_served = number_served
        
    def increment_number_served(self, increment):
        """
        Increment the number of customers that have been served by a given amount.
        """
        self.number_served += increment
        print(f"The number of customers served is now {self.number_served}")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, flavors = []):
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        """
        Display the flavors of ice cream.
        """
        print(f"The flavors of ice cream are: {self.flavors}")

# restaurant = Restaurant("The Pizza Palace", "Pizza")

# print(restaurant.name)
# print(restaurant.cuisine_type)

# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# restaurant_1 = Restaurant("The Kebab Palace", "Kebab")
# restaurant_2 = Restaurant("The Burger Palace", "Burger")
# restaurant_3 = Restaurant("The Fish Palace", "Fish")

# restaurant_1.describe_restaurant()
# restaurant_2.describe_restaurant()
# restaurant_3.describe_restaurant()

restaurant = Restaurant("The Pizza Palace", "Pizza")
ice_rio = IceCreamStand("Ice Rio", "Ice Cream")

ice_rio.display_flavors()

print(restaurant.number_served)
# restaurant.number_served = 10
restaurant.set_number_served(10)

print(restaurant.number_served)

restaurant.increment_number_served(5)