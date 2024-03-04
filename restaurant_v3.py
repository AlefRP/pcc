class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        
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
        
# restaurant = Restaurant("The Pizza Palace", "Pizza")

# print(restaurant.name)
# print(restaurant.cuisine_type)

# restaurant.describe_restaurant()
# restaurant.open_restaurant()

restaurant_1 = Restaurant("The Kebab Palace", "Kebab")
restaurant_2 = Restaurant("The Burger Palace", "Burger")
restaurant_3 = Restaurant("The Fish Palace", "Fish")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
        