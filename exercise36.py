"""
List Remove Duplicates
Exercise 14

Write a program (function!) that takes a list and returns a new list
that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""

#Solution using a loop:

thislist = ["apple", "banana", "cherry", "raspberry", "cherry", "apple", "pineapple"]

def removeduplicates(input):
    output = []
    for x in input:
        if x not in output:
            output.append(x)
    print(output)

#Solution using sets:

def removeduplicates(input):
    return list(set(input))

