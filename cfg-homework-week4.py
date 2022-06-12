"""
Write a function named "recap" that:
1. Takes one argument called "aNumber"
2. loops from 0 until and including the argument "aNumber"
3. If it finds the value 42, prints out "Found the meaning of life!"
4. If no value 42 was found it prints "Did not find 42 - sadface" only one.
Prompt the user for a number and pass it into the function "recap".
"""

def recap(aNumber):
    num = int(aNumber)
    for x in range(num+1):
        if x == 42:
            print("Found the meaning of life!")
            quit()
    print("Did not find 42 - sadface")

aNumber = input('Pick a number: ')
recap(aNumber)

"""
I have a list of things I need to buy from my supermarket of choice.
shopping_list = ["oranges",
                "cat food",
                "sponge cake",
                "long-grain rice",
                "cheese board",
                ]
print(shopping_list[1])
I want to know what the first thing I need to buy is.
However, when I run the program it shows me a different answer to what I was expecting?
What is the mistake? How do I fix it?
"""
shopping_list = ["oranges",
                "cat food",
                "sponge cake",
                "long-grain rice",
                "cheese board",
                ]

print(shopping_list[1])

#The list is indexed from 0, so to print the first item, you should write:
print(shoppinglist[0])

"""
I'm setting up my own market stall to sell chocolates.'
I need a basic till to check the prices of different chocolates that I sell.
I've started the program and included the chocolates and their prices.'
Finish the program by asking the user to input an item and then output its price.
"""

chocolates = {'white': 1.50, 'milk': 1.20,'dark': 1.80, 'vegan': 2.00}
choice = input('What chocolate would you like? ')
output = chocolates[choice]
print(f"That will cost £{output}")

"""
Question 3
Write a program that simulates a lottery.
The program should have a list of seven numbers that represent a lottery ticket.
It should then generate seven random numbers.
After comparing the two sets of numbers, the program should output a prize based on the number of matches:
    ● £20 for three matching numbers
    ● £40 for four matching numbers
    ● £100 for five matching numbers
    ● £10000 for six matching numbers
    ● £1000000 for seven matching numbers
"""

import random
ticket = [3, 11, 99, 43, 6, 21, 88]
random_numbers = []
total_match = 0
for x in range(7):
    random_numbers.append(random.randrange(0,101))
print(random_numbers)
for y in range(7):
    if random_numbers[y] in ticket:
        total_match += 1
if total_match <3:
    print("Bad luck!")
elif total_match == 3:
    print("You win £20!")
elif total_match == 4:
    print("You win £40!")
elif total_match == 5:
    print("You win £100!")
elif total_match == 6:
    print("You win £10,000!")
elif total_match == 7:
    print("You win £1,000,000!")
