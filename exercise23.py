'''Create a program that asks the user for a number and then prints out a list of all the divisors of that number.'''

sval = input('Pick a number: ')
ival = int(sval)

x = 1
while x <= ival:
    if ival % x == 0:
        print(x)
    x = x + 1