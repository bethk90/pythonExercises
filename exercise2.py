'''

Print the following pattern
Write a program to print the following number pattern using a loop.

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

'''

x = 1
output = ''

while x < 6:
    output = str(output) + ' ' + str(x)
    print(output)
    x = x + 1