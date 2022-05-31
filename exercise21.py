'''
You have been asked to make a book categorisation programme, which assigns each book a special code based on its title.
The code is equal to the first letter of the book, followed by the number of characters in the title.
For example, for the book "Harry Potter", the code would be: H12, as it contains 12 characters (including a space.)
You are provided a books.txt file, which includes the book titles, each one written on a separate line.
Read the title one by one and output the code for each book on a separate line.
'''

filename = input('Enter file name: ')
fhand = open(filename)
for line in fhand:
    firstletter = line[0]
    length = len(line) -1
    code = firstletter + str(length)
    print(code)