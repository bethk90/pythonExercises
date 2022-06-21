"""5. Hangman

The Goal: Despite the name, the actual “hangman” part isn’t necessary.
The main goal here is to create a sort of “guess the word” game.
The user needs to be able to input letter guesses.
A limit should also be set on how many guesses they can use.
This means you’ll need a way to grab a word to use for guessing.
This can be grabbed from a pre-made list. No need to get too fancy.)
You will also need functions to check if the user has actually inputted a single letter,
to check if the inputted letter is in the hidden word (and if it is, how many times it appears),
to print letters, and a counter variable to limit guesses.
"""
import random

def hangman():
    guess_count = 0
    blank_list = ['-', '-', '-', '-', '-']
    getwords = open('randomwords.txt', 'r')
    n = random.randint(0,150)
    words = [word for word in getwords]
    randomword = words[n][:-1]
    list_letters_in_word = list(randomword)
    while True:
        user_guess = input('Guess a five-letter word: ')
        guess_count += 1
        letters_in_guess = set(user_guess)
        if user_guess ==
        if user_guess == randomword:
            print(f'You win! You guessed in {guesscount} guesses.')
            break
        else:
            for letter in list_letters_in_word:
                if letter in letters_in_guess:
                    letterpos = list_letters_in_word.index(letter)
                    blank_list[letterpos] = letter
                    list_letters_in_word[letterpos] = '-'
        blank = ''.join(blank_list)
        print(blank)

hangman()