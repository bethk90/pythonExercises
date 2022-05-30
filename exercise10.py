'''
Write a program to use for loop to print the following reverse number pattern

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
'''

x = 5

for number in range(x, 0, -1):
    print(*range(x, 0, -1))
    x = x -1