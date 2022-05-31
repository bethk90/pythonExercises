"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.
"""

def is_it_prime():
    num = int(input('Enter a number: '))
    x = 2
    while True:
        if x < num:
            if num % x == 0:
                print(f'This number is not prime, it divides by {x}.')
                break
            else:
                x = x + 1
                continue
        else:
            print('This number is prime')
            break

is_it_prime()