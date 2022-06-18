"""Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many
messages have come from each email address, and print the dictionary."""

def emailaddresses():
    fhand = open('mbox-short.txt')
    counts = dict()
    for line in fhand:
        wds = line.split()
        if len(wds) > 0:
            if wds[0] == 'From:':
                counts[wds[1]] = counts.get(wds[1],0) + 1
    print(counts)

"""Exercise 4: Add code to the above program to figure out who has the most messages in the file.
After all the data has been read and the dictionary has been created,
look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops)
to find who has the most messages and print how many messages the person has.
"""

def emailaddresses2():
    fhand = open('mbox-short.txt')
    counts = dict()
    max = 0
    for line in fhand:
        wds = line.split()
        if len(wds) > 0:
            if wds[0] == 'From:':
                counts[wds[1]] = counts.get(wds[1],0) + 1
    for item in counts:
        if counts.get(item) > max:
            max = counts.get(item)
            biggest = item

    print(biggest, max)

"""Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of
who the mail came from (i.e., the whole email address).
At the end of the program, print out the contents of your dictionary."""

def emailaddresses3():
    fhand = open('mbox-short.txt')
    counts = dict()
    for line in fhand:
        wds = line.split()
        if len(wds) > 0:
            if wds[0] == 'From:':
                domain = wds[1][wds[1].find('@') + 1:]
                counts[domain] = counts.get(domain, 0) + 1
    print(counts)

emailaddresses()
emailaddresses2()
emailaddresses3()