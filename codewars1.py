"""Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid."""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def high(x):
    wordlist = x.split(' ')
    listlength = len(wordlist)
    highestscore = 0
    highestword = ''
    for index in range(listlength):
        total = 0
        y = wordlist[index]
        wordlength = len(y)
        for letter in range(wordlength):
            letterscore = (alphabet.index(y[letter]) + 1)
            total += letterscore
            continue
        if total > highestscore:
            highestscore = total
            highestword = y
            continue
    return highestword
