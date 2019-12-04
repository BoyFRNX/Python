from random import randint


class Die:
    """A simple representation of how dice work."""

    def __init__(self, sides=6):
        """Initializes the sides attribute and sets the default value to 6."""
        self.sides = sides

    def roll_die(self):
        """Rolls a random number between 1 and the number of sides."""

        return randint(1, self.sides)


six_sided = Die()
ten_sided = Die(10)
twenty_sided = Die(20)


def roll_x_times(die_name, num_of_rolls):
    """Rolls given die 10 times and prints returned value."""
    count = 0
    print(f"Rolling die...")
    while count < num_of_rolls:
        count += 1
        number = die_name.roll_die()
        print(f"Roll #{count}: {number}")


roll_x_times(six_sided, 10)
roll_x_times(ten_sided, 10)
roll_x_times(twenty_sided, 10)
