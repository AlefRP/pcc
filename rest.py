"Class that describes a restaurant"
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