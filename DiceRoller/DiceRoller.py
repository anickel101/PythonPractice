import random

min = 1
max = 6
num_dice = 1

roll_again = "y"

while roll_again == "y":

    num_dice = int(raw_input("How many dice are you rolling? (1-6)"))

    print "Rolling dice..."
    print "The values are..."

    index = int(0)

    while index < num_dice:
        roll = random.randint(min, max)
        num = index + 1
        print "Die {num} is: {roll}".format(num=num, roll=roll)
        index += 1

    roll_again = raw_input("Roll the dice again? (y/n)")
