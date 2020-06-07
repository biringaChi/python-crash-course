# Q.9-13: Ordered dictionaries
from collections import OrderedDict

def ordered_dict():
    rivers_countries = OrderedDict()
    rivers_countries["nile"] = "egypt"
    rivers_countries["amazon"] = "south america"
    rivers_countries["ganges"] = "india"
    rivers_countries["mississippi"] = "united states of america"
    rivers_countries["danube"] = "europe"
    for river, country in rivers_countries.items():
        if river in "mississippi":
            print(f"The {river.title()} river is in the {country.title()}")
        else:
            print(f"The {river.title()} river is in {country.title()}")

# ordered_dict()

# Help available to the variable
# print(dir(rivers_countries))
# help availabe to string
# print(help(str))
# help availabe to specific method to string
# print(help(str.lower))
# print(help(OrderedDict))

"""
# Q.9-14. Dice: The module random contains functions that generate random num- bers in a variety of ways.
The function randint() returns an integer in the range you provide. The following code returns a number between 1 and 6:
"from random import randint" x = randint(1, 6) Make a class Die with one attribute called sides, which has a default value of 6.
Write a method called roll_die() that prints a random number between 1 and the number of sides the die has .
Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die . Roll each die 10 times.
"""

from random import randint

class Die():
    """ simulating a roll of a die """
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        x = randint(1, 6)
        return f"Random number {x} of a {self.sides} sided die"

    def six_sided_die(self, six_sides):
        if self.sides == six_sides:
            print("A 6-sided die rolled ten times")
            for rolls in range(10):
                six_sides = randint(1, 6)
                print(f"Roll {rolls} = {six_sides}")

    def ten_side_die(self, ten_sides):
        if self.sides != ten_sides:
            print("A 10-sided die rolled ten times")
            for rolls in range(10):
                ten_rand = randint(1, 10)
                print(f"Roll {rolls} = {ten_rand}")

    def twenty_side_die(self, twenty_sides = 20):
        if self.sides != twenty_sides:
            print("A 20-sided die rolled ten times")
            for enu,  _ in enumerate(range(10)):
                twenty_rand = randint(1, 20)
                print(f"Roll {enu} = {twenty_rand}")

# die = Die()
# die.ten_side_die(ten_sides = 10)
# die.twenty_side_die(twenty_sides = 20)
