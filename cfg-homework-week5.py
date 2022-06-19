"""In this session you used the Pokemon API to retrieve a single Pokemon.
I want a program that can retrieve myltiple Pokemon and save their names and moves to a
if file:

Use a list to store about 6 Pokemon IDs.
Then in a for loop call the API to retrieve the data for each Pokemon.
Save their names and moves into a file called 'pokemon.txt'.

"""

import requests

poke_list = ['pikachu', 'charizard', 'squirtle', 'ditto', 'bulbasaur', 'eevee']

def get_pokemon():
    for item in poke_list:
        url = f'https://pokeapi.co/api/v2/pokemon/{item}/'
        response = requests.get(url)
        pokemon = response.json()
        poke_moves = pokemon['moves']
        move_list = []
        for move in poke_moves:
            move_list.append(move['move']['name'])
        formatted_list = '\n'.join(move_list)
        with open('pokemon.txt', 'a') as poke_file:
            poke_file.write(f'{item.title()}\'s moves are:\n{formatted_list}.\n')

get_pokemon()