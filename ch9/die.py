#Dice class, import example

from random import randint

class Die():
  def __init__(self, sides = 6):
    self.sides = sides

  def roll_die(self):
    sides = str(self.sides)
    randomNumber = str(randint(1, self.sides))
    print("Rolled: " + randomNumber + " , " + "Sides: " + sides )

die = Die()

for x in range(1,10):
  die.roll_die()

die2 = Die(10)

for x in range(1,10):
  die2.roll_die()
