'''
I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can make. Write a program to calculate this.
Assume that a box of eggs contains six eggs and I need four eggs for each omelette, but I should be able to easily change these values if I want.
The output should say something like "You can make 9 omelettes with 6 boxes of eggs".
'''

egg_boxes = 6
eggs_per_box = 6
eggs_per_omelette = 4
omelette_total = (egg_boxes * eggs_per_box)/eggs_per_omelette
message = ('You can make {} omelettes with {} boxes of eggs').format(omelette_total, egg_boxes)

print(message)