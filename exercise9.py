'''
Count the total number of digits in a number
Write a program to count the total number of digits in a number using a while loop.

For example, the number is 75869, so the output should be 5.
'''

count = 0
num = input('Number: ')

while count < len(num):
    count = count + 1

print(f"The length is {count}")