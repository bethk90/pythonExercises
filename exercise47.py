"""
Write a password generator in Python.
Be creative with how you generate passwords -
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

"""
import string
import random
from random import randint

alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)
symbol_list = list('!@#$%^&*()_')

strength = input('How strong do you want your password to be? Weak/Medium/Strong: ')

def password_generator(strength):
    if strength == 'Weak':
        password = random.choice(open("randomwords.txt").read().split())
    if strength == 'Medium':
        word = random.choice(open("randomwords.txt").read().split())
        password = ''
        for letter in word:
            v = randint(0,10)
            if v % 2 == 0:
                letter = letter.upper()
            password += letter
        i = randint(0,10)
        password += str(i)
    if strength == 'Strong':
        password = ''
        n = 0
        while n < 6:
            a = randint(0,10)
            if a % 2 == 0:
                b = randint(0, 25)
                z = alphabet_list[b]
                c = randint(0,10)
                if c % 2 == 0:
                    z = z.upper()
            else:
                z = str(randint(0, 10))
            password += z
            n += 1
    print(f"Your password is: '{password}'")

password_generator(strength)
