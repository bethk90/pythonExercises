"""The Goal: The program will first prompt the user for a series of inputs a la Mad Libs.
For example, a singular noun, an adjective, etc.
Then, once all the information has been inputted, the program will take that data and place them into
a premade story template. You’ll need prompts for user input,
and to then print out the full story at the end with the input included."""

def madlibs():
    number_1 = input('Enter a number: ')
    time_2 = input('Pick a length of time: ')
    transport_3 = input('Choose a mode of transport: ')
    adjective_4 = input('Select an adjective: ')
    adjective_5 = input('Select another adjective: ')
    noun_6 = input('Think of a random noun: ')
    colour_7 = input('What\'s your favourite colour? ')
    body_8 = input('Think of a body part: ')
    verb_9 = input('Pick a verb: ')
    number_10 = input('Choose a number: ')
    noun_11 = input('Select a noun: ')
    noun_12 = input('Select another noun: ')
    body_13 = input('Think of a body part: ')
    verb_14 = input('Choose a verb: ')
    noun_15 = input('Select a noun: ')
    adj_16 = input('Think of an adjective: ')
    silly_17 = input('Think of a silly word: ')
    noun_18 = input('And finally, another noun: ')

    print(
         f'It was about {number_1} {time_2} ago when I came to the hospital in a {transport_3}. The hospital is a {adjective_4} place, there are a lot of {adjective_5} {noun_6}s here.'
        f'There are nurses here who have {colour_7} {body_8}s. If someone wants to come into my room, I told them that they have to {verb_9} first.'
        f'I have decorated my room with {number_10} {noun_11}s.'
        f'Today a doctor came into my room and they were wearing a {noun_12} on their {body_13}.'
        f'I heard that all doctors {verb_14} {noun_15} every day for breakfast.'
        f'The most {adj_16} thing about being in the hospital is the {silly_17} {noun_18}!')

madlibs()