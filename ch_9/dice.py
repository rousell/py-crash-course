from random import randint

class Dice():
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_dice(self):
        print(str(randint(1, self.sides)))

print("\n6 sided dice")
basic_dice = Dice()
basic_dice.roll_dice()
basic_dice.roll_dice()
basic_dice.roll_dice()
basic_dice.roll_dice()
basic_dice.roll_dice()
basic_dice.roll_dice()
basic_dice.roll_dice()
basic_dice.roll_dice()
basic_dice.roll_dice()
basic_dice.roll_dice()

print("\n10 sided dice")
ten_sided_dice = Dice(10)
ten_sided_dice.roll_dice()
ten_sided_dice.roll_dice()
ten_sided_dice.roll_dice()
ten_sided_dice.roll_dice()
ten_sided_dice.roll_dice()
ten_sided_dice.roll_dice()
ten_sided_dice.roll_dice()
ten_sided_dice.roll_dice()
ten_sided_dice.roll_dice()
ten_sided_dice.roll_dice()

print("\n20 sided dice")
twenty_sided_dice = Dice(20)
twenty_sided_dice.roll_dice()
twenty_sided_dice.roll_dice()
twenty_sided_dice.roll_dice()
twenty_sided_dice.roll_dice()
twenty_sided_dice.roll_dice()
twenty_sided_dice.roll_dice()
twenty_sided_dice.roll_dice()
twenty_sided_dice.roll_dice()
twenty_sided_dice.roll_dice()
twenty_sided_dice.roll_dice()