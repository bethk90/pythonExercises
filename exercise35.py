"""
Write a program that reads the words in words.txt and stores them as keys in a dictionary.
It doesn’t matter what the values are.
Then you can use the in operator as a fast way to check whether a string is in the dictionary.

"""

handle = open('words.txt')

counts = dict()
for line in handle:
    wds = line.split()
    for wd in wds:
        counts[wd] = counts.get(wd,0) + 1

def checkword(word):
    if word in counts:
        print(f'{word} is in the file {counts[word]} times')
    else:
        print(f'{word} is not in the file')

word = input('Check this word: ')
checkword(word)