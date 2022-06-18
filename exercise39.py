#Find 5 most common words in text file.

def countwords():
    filename = input('Enter file name: ')
    fhand = open(filename)
    counts = dict()
    max = 0
    lst = list()
    for line in fhand:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word,0) + 1
    for item in counts:
        if counts.get(item) > max:
            max = counts.get(item)
            common = item

    for key,val in list(counts.items()):
        lst.append((val,key))

    lst.sort(reverse=True)

    for key,val in lst[:5]:
        print(key,val)

countwords()