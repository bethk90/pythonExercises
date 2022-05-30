smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 2, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

biggest = None
for x in (1.2, 3, 4, 0.7, 10, 4.1, 0.2):
    if biggest is None:
        biggest = x
    elif biggest < x:
        biggest = x
    print("I've checked " + str(x) + f" and the biggest is {biggest}")
