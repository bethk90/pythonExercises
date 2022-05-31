"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random

def guessing_game():
    while True:
        count = 0
        num = random.randint(1, 9)
        print(num)
        usernum = input('Guess a number: ')
        if usernum == 'exit':
            print('Thanks for playing!')
            break
        try:
            guess = int(usernum)
        except:
            print('Invalid data, sorry!')
            continue
        while True:
            count = count + 1
            if guess == num:
                print(f'Correct! Thanks for playing! Guess count: {count}')
                break
            elif guess > num:
                print('Too high!')
            elif guess < num:
                print('Too low')
            usernum = input('Guess a number: ')
            guess = int(usernum)
        playagain = input('Play again Y/N? ')
        if playagain == 'N':
            print('Play again soon!')
            break

guessing_game()

 #   guess = int(usernum)
  #  if usernum == 'break':
  #      break
  #  while True:
  #      elif guess == num:
#            print('Correct!')
 #       elif guess > num:
  #              print('Too high!')
   #     elif guess < num:
    #            print('Too low!')
#
 #   count = count + 1
  #  num = random.randint(0, 9)
