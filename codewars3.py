"""You are going to be given a word.
Your job is to return the middle character of the word.
If the word's length is odd, return the middle character.
If the word's length is even, return the middle 2 characters.
"""

def get_middle(s):
    slist = list(s)
    l = len(slist)
    return ''.join(slist[int(l/2 -1):int(l/2 +1)]) if l % 2 == 0 else slist[int((l/2)-.5)]
