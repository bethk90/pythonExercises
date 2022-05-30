'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year).
If you want to do this in a generic way, see exercise 39.
'''

name = input('What is your name? ')
age = input('What is your age? ')

def when100():
    yearstogo = 100 - int(age)
    when = 2022 + yearstogo
    print(f"You will turn 100 in the year {when}, {name}")

when100()
