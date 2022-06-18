"""Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done.
To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the
days of the week. At the end of the program print out the contents of your dictionary (order does not matter).
"""

def daysoftheweek():
    fhand = open('mbox-short.txt')
    counts = dict()
    for line in fhand:
        wds = line.split()
        if len(wds) > 2:
            if wds[0] == 'From':
                counts[wds[2]] = counts.get(wds[2],0) + 1
    print(counts)

daysoftheweek()