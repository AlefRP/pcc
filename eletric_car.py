class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """In'itialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """Define a method to set the odometer reading."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
    def fill_gas_tank(self):
        """Fill the gas tank."""
        print("Filling the gas tank...")

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size == 40:
            self.battery_size = 65
            print("Upgraded the battery to 65 kWh.")
        
    def get_range(self):    
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 220
        print(f"This car can go about {range} miles on a full charge.")
        
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        # self.battery_size = 40
    
    # def describe_battery(self):
    #     """Print a statement describing the battery size."""
    #     print(f"This car has a {self.battery_size}-kWh battery.")
        
    def fill_gas_tank(self): # Subscring to the parent method
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
        
my_leaf = ElectricCar('tesla', 'leaf', 2019)
print(my_leaf.get_descriptive_name())
# my_leaf.describe_battery()
my_leaf.battery.describe_battery() # Subscring to the child method
my_leaf.battery.get_range() # Subscring to the child method
my_leaf.fill_gas_tank()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()