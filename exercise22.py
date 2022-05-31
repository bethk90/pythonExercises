'''Ask the user for a number.
Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.

sval = input('Choose a number: ')
ival = int(sval)

if ival % 2 == 0:
    if ival % 4 == 0:
        print("Nice, a multiple of 4")
    else:
        print("That's an even number!")
else:
    print("That's an odd number!")

'''

#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = input('Choose a number: ')
check = input('What shall I divide it by? ')
inum = int(num)
icheck = int(check)

if inum % icheck == 0:
    print(f"{icheck} divides evenly into {inum}")
else:
    print(f"{icheck} doesn't divide evenly into {inum}")