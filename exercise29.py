"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random

num = random.randint(0, 9)

while True:

    try:
        usernum = int(input('Guess a number: '))
    except:
        print('Invalid data')

    if usernum == num:
        print('Correct!')
        break

    else:
        if usernum > num:
            print('Too high!')
        elif usernum < num:
            print('Too low!')