#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = input("How many hours did you work? ")
rate = input("What is your hourly rate? ")
hours = float(hours)
rate = float(rate)

if hours > 40:
    overtime = hours - 40
    pay = (40 * rate) + (overtime * rate * 1.5)
else:
    pay = hours * rate

print("Your pay is ",pay)

hours = input("How many hours did you work? ")
rate = input("What is your hourly rate? ")

#Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.

try:
    hours = float(hours)
    rate = float(rate)
    if hours > 40:
        overtime = hours - 40
        pay = (40 * rate) + (overtime * rate * 1.5)
    else:
        pay = hours * rate
    print("Your pay is ",pay)

except:
    print("please enter numeric input")
    quit()

'''
Rewrite your pay computation with time and-a-half for overtime and create a function
called computepay which takes two parameters (hours and rate)
'''

def computepay(hours, rate):
    if hours > 40:
        overtime = hours - 40
        pay = (40 * rate) + (overtime * rate * 1.5)
    else:
        pay = (40 * rate) + (overtime * rate * 1.5)
    print("Your pay is ", pay)

computepay(45,10)