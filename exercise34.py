"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

"""

num = input('Pick a number: ')

def fibonacci(num):
    length = int(num) -1
    x = 1
    num1 = 1
    num2 = 1
    sequence = [num1, num2]
    while x < length:
        num3 = num1 + num2
        sequence.append(num3)
        num1 = num2
        num2 = num3
        x = x + 1
    print('Length: ', length)
    print('X: ', x)
    print(sequence)

fibonacci(num)