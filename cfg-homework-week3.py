"""
Create a program that tells you whether or not you need an umbrella when you leave the house.
The program should:

1.Ask you if it is raining using input()

2.If the input is 'y', it should output 'Take an umbrella'

3.If the input is 'n', it should output 'You don't need an umbrella'

"""


def umbrella(is_raining):
    if is_raining == 'y':
        print('Take an umbrella')
    else:
        print('You don\'t need an umbrella')


is_raining = input('Is it raining? y/n: ')

umbrella(is_raining)

"""

I'm on holiday and want to hire a boat.
The boat hire costs £20 + a refundable £5 deposit.
I've written a program to check that I can afford the cost, but something doesn't seem right.
Have a look at my program and work out what I've done wrong

my_money = input('How much money do you have? ')
boat cost = 20 + 5
if my_money < boat_cost:
	print('You can afford the boat hire')
else:
	print('You cannot afford the board hire')

"""

my_money = input('How much money do you have? ')
boat_cost = 20 + 5
if int(my_money) >= boat_cost:
    print('You can afford the boat hire')
else:
    print('You cannot afford the boat hire')

"""

Your friend works for an antique book shop that sells books between 1800 and 1950 and wants to quickly categorise
books by the century and decade that they were written.
Write a program that takes a year (e.g. 1872) and outputs the century and decade
(e.g. "Eighteenth Century, Seventies")

"""


def categorise(year):
    if year[0:2] == '18':
        century = 'Eighteenth Century'
    if year[0:2] == '19':
        century = 'Nineteenth Century'
    if year[2] == '0':
        decade = 'Noughties'
    if year[2] == '1':
        decade = 'Teens'
    if year[2] == '2':
        decade = 'Twenties'
    if year[2] == '3':
        decade = 'Thirties'
    if year[2] == '4':
        decade = 'Fourties'
    if year[2] == '5':
        decade = 'Fifties'
    if year[2] == '6':
        decade = 'Sixties'
    if year[2] == '7':
        decade = 'Seventies'
    if year[2] == '8':
        decade = 'Eighties'
    if year[2] == '9':
        decade = 'Nineties'
    output = f"{century}, {decade}"
    print(output)


year = input('What year was the book published? ')

categorise(year)

