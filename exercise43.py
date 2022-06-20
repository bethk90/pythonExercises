"""4. TextBased Adventure Game

The Goal: Remember Adventure? Well, we’re going to build a more basic version of that.
A complete text game, the program will let users move through rooms based on user input
and get descriptions of each room.
To create this, you’ll need to establish the directions in which the user can move,
a way to track how far the user has moved (and therefore which room he/she is in),
and to print out a description.
You’ll also need to set limits for how far the user can move.
In other words, create “walls” around the rooms that tell the user, “You can’t move further in this direction.”
Concepts to keep in mind:

Strings
Variables
Input/Output
If/Else Statements
Print
List
Integers

The tricky parts here will involve setting up the directions and keeping track of just how far the user has “walked” in the game.
I suggest sticking to just a few basic descriptions or rooms, perhaps 6 at most.
This project also continues to build on using userinputted data.
It can be a relatively basic game, but if you want to build this into a vast, complex word,
the coding will get substantially harder, especially if you want your user to start interacting
with actual objects within the game.
That complexity could be great, if you’d like to make this into a longterm project.
"""

tube_map = [

    {'name': 'Victoria Line',
    'stations': [
        {
            'name': 'Walthamstow Central',
            'lines': ['Victoria Line']
        },
        {
            'name': 'Blackhorse Road',
            'lines': ['Victoria Line']
        },
        {
            'name': 'Tottenham Hale',
            'lines': ['Victoria Line']
        },
        {
            'name': 'Seven Sisters',
            'lines': ['Victoria Line']
        },
        {
            'name': 'Finsbury Park',
            'lines': ['Victoria Line', 'Piccadilly Line']
        },
        {
            'name': 'Highbury & Islington',
            'lines': ['Victoria Line']
        },
        {
            'name': 'King\'s Cross St Pancras',
            'lines': ['Victoria Line', 'Piccadilly Line', 'Northern Line', 'Circle Line', 'Metropolitan Line',
                      'Hammersmith and City Line']
        },
        {
            'name': 'Euston',
            'lines': ['Victoria Line', 'Northern Line']
        },
        {
            'name': 'Warren Street',
            'lines': ['Victoria Line', 'Northern Line']
        },
        {
            'name': 'Oxford Circus',
            'lines': ['Victoria Line', 'Bakerloo Line', 'Central Line']
        },
        {
            'name': 'Green Park',
            'lines': ['Victoria Line', 'Piccadilly Line', 'Jubilee Line']
        },
        {
            'name': 'Victoria',
            'lines': ['Victoria Line', 'Circle Line', 'District Line']
        },
        {
            'name': 'Pimlico',
            'lines': ['Victoria Line']
        },
        {
            'name': 'Vauxhall',
            'lines': ['Victoria Line']
        },
        {
            'name': 'Stockwell',
            'lines': ['Victoria Line', 'Northern Line']
        },
        {
            'name': 'Brixton',
            'lines': ['Victoria Line']
        }
    ]
     },

    {'name': 'Piccadilly Line',
    'stations': [
        {
            'name': 'Cockfosters',
            'lines': ['Piccadilly Line']
        },
        {
            'name': 'Oakwood',
            'lines': ['Piccadilly Line']
            },
        ]
     }
]



def tfl():
    while True:
        current_line = input('Which line are you taking? ')
        line_names = [line['name'] for line in tube_map]
        #Can the line below be simplified?
        list_line_names = ', '.join([line['name'] for line in tube_map])

        if current_line not in line_names:
            print(f'That\'s not a line, the options are: {list_line_names}.')
            continue

        for line in tube_map:
            if current_line == line['name']:
                current_station = input('Which station are you getting on at? ')
                while True:
                    station_list = list(line['stations'])
                    if current_station not in station_list:
                        #This needs fixing to print out the list as a string
                        print(f'That\'s not a station, the options are: {station_list}.')
                        break
                    else:
                        for station in line['stations']:
                            if (station['name']) == current_station:
                                #station_list = list(line['stations'])
                                print(f'You are at {current_station}.')
                                available_stations = ', '.join(station['lines'])
                                print(f'You can take any of these lines: {available_stations}')
                                direction = input('Which direction are you travelling? ')
                                stops = input('How many stops are you going? ')
                                stationpos = station_list.index(station)
                                if direction == 'Northbound':
                                    stationpos -= int(stops)
                                    current_station = station_list[stationpos]['name']
                                if direction == 'Southbound':
                                    stationpos += int(stops)
                                    current_station = station_list[stationpos]['name']

tfl()
