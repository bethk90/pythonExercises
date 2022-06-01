"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the
first and last elements of the given list. For practice, write this code inside a function.
"""

a = [1, 5, 10, 15, 20, 25, 30]

def firstlast(list):
    newlist = []
    last = len(list) - 1
    newlist.append(str(list[0]))
    newlist.append(str(list[last]))
    print(newlist)

firstlast(a)
