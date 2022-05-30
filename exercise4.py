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

def computepay(hours, rate):
    if hours > 40:
        overtime = hours - 40
        pay = (40 * rate) + (overtime * rate * 1.5)
    else:
        pay = (40 * rate) + (overtime * rate * 1.5)
    print("Your pay is ", pay)

computepay(45,10)