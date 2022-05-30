'''
Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop

Given:

numbers = [12, 75, 150, 180, 145, 525, 50]
Expected output:

75
150
145

'''

for x in [12, 75, 150, 180, 145, 525, 50]:
    if x % 5 == 0:
        if x > 500:
            break
        if x <= 150:
            print(x)
        elif x > 150:
            continue
