alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_incrementa = 1
elif alien_0['speed'] == 'medium':
    x_incrementa = 2
else:
    x_incrementa = 3
print("New x-position: " + str(alien_0['x_position']))
del alien_0['speed']
print(alien_0)

