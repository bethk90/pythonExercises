'''
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''

string = input('Pick a word: ')
length = len(string) - 1
if string[::] == (string[length::-1]):
    print('Palindrome!')
else:
    print('Not a palindrome!')