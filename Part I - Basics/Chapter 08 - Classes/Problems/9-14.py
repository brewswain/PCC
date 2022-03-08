from random import randint


class Die():
    """Representation of dice of multiple sides"""

    def __init__(self, sides=6):
        """Initialise die instances"""
        self.sides = sides

    def roll_dice(self):
        """Simulate dice rolling."""
        roll = randint(1, self.sides)
        return roll


rolls = []
d6 = Die()

print('')
for roll in range(10):
    roll_result = d6.roll_dice()
    rolls.append(roll_result)
print("10d6 roll?! Let's see how much damage you got:")
print(rolls)
print(str(sum(rolls)) + " damage dealt.")

print('')
d10 = Die(10)
for roll in range(10):
    roll_result = d10.roll_dice()
    rolls.append(roll_result)
print("10d10 roll?! Let's see how much damage you got:")
print(rolls)
print(str(sum(rolls)) + " damage dealt.")

print('')
d20 = Die(20)
for roll in range(10):
    roll_result = d20.roll_dice()
    rolls.append(roll_result)
print("10d20 roll?! If you miss this...")
print(rolls)
