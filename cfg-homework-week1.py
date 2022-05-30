egg_boxes = 6
eggs_per_box = 6
eggs_per_omelette = 4
omelette_total = (egg_boxes * eggs_per_box)/eggs_per_omelette
message = ('You can make {} omelettes with {} boxes of eggs').format(omelette_total, egg_boxes)

print(message)