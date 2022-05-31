'''
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''

def rock_paper_scissors(player1, player2):
    options = ['scissors', 'paper', 'rock']

    player1 = player1.lower()
    player2 = player2.lower()

    if player1 not in options:
        print('That\'s not an option, Player 1')
    elif player2 not in options:
        print('That\'s not an option, Player 2')
    else:
        print('Let battle commence!')

    if player1 == 'rock':
        if player2 == 'rock':
            print('Draw!')
        elif player2 == 'scissors':
            print('Player 1 wins!')
        elif player2 == 'paper':
            print('Player 2 wins!')

    if player1 == 'paper':
        if player2 == 'rock':
            print('Player 1 wins!')
        elif player2 == 'paper':
            print('Draw!')
        elif player2 == 'scissors':
            print('Player 2 wins!')

    if player1 == 'scissors':
        if player2 == 'rock':
            print('Player 2 wins!')
        elif player2 == 'paper':
            print('Player 1 wins!')
        elif player2 == 'scissors':
            print('Draw!')

while True:
    player1 = input('Choose your weapon, Player 1: ')
    player2 = input('Choose your weapon, Player 2: ')
    rock_paper_scissors(player1, player2)
    prompt = input('Play again? Y/N: ')
    if prompt == 'Y':
        continue
    else:
        print('Thanks for playing!')
        break
