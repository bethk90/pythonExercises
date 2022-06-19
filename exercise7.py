'''
Write a programme which repeatedly reads numbers until the user enters "done".
Once "done" is entered, print out the total, count, and average of the numbers.
If the user enters anything other than a number, detect their mistake using try and except, and print an error message and skip to the next number.
'''

count = 0
total = 0

while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    try:
        number = int(number)
    except:
        print('Sorry bad data')
        continue
    count = count + 1
    total = total + number
    ave = total/count

print('all done')
print(str(total), str(count), str(ave))

"""Exercise 2: Write another program that prompts for a list of numbers as above
and at the end prints out both the maximum and minimum of the numbers instead of the average."""

max = None
min = None

while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    try:
        number = int(number)
        if max is None:
            max = number
        elif number > max:
            max = number
        if min is None:
            min = number
        elif number < min:
            min = number
    except:
        print('Sorry bad data')
        continue

print('all done')
print(f"The largest number is {max} and the smallest number is {min}.")