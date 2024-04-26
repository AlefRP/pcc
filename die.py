from random import randint

class Die:
    """A class representing a single die."""

    def __init__(self, sides=6):
        """Assume a six-sided die."""
        self.sides = sides

    def roll_die(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.sides)
    
my_die_six = Die()
my_die_ten = Die(10)
my_die_twenty = Die(20)

current_die = [my_die_six, my_die_ten, my_die_twenty]

# Rolling three 6-sided, 10-sided, and 20-sided dies
for die in current_die:
    print(f"Rolling a {die.sides}-sided die...")
    for roll_num in range(10):
        print(f"Roll #{roll_num+1}: {die.roll_die()}")