aliens = []  # cria uma lista vazia para armazenar alienígenas
for alien_number in range(30):  # cria trinta alienígenas verdes
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    for alien in aliens[:5]:  # mostra os 5 primeiros alienígenas
        print(alien)
        print("...")
print("Total number of aliens: " + str(len(aliens)))
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
        print(alien)
        print("...")
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
        print(alien)
