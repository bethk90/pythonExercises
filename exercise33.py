#Debug this code

han = open('mbox-short.txt')

while True:
    for line in han:
        line = line.rstrip()
        wds = line.split()
        if len(wds) == 0:
            continue
        if wds[0] != 'From':
            continue
        print(wds[2])