"""
Exercise 15 (and Solution)
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.

For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My

shown back to me.


"""

def reverse_word_order(string):
    slist = string.split()
    print (' '.join(slist[::-1]))

reverse_word_order('My name is Michele')