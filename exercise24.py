'''
Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in a:
  if x < 5:
    print(x)

#Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for x in a:
  if x < 5: b.append(x)
print(b)

#Write this in one line of Python.

b = [x for x in a if x < 5]
print(b)

#Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = input('Pick a number: ')
ic = int(c)

for x in a:
  if x < ic: b.append(x)
print(b)