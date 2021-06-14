minhas_pizzas = ['mussarela', 'calabresa', 'portuguesa', 'lombinho']
friend_pizzas = minhas_pizzas[:]
minhas_pizzas.append('frango com catupiri')
friend_pizzas.append('bolonhesa')

pizza = [pizzas for pizzas in minhas_pizzas]
print(f"Minhas pizzas favoritas são:{pizza}\n")

pizza_dos_amigos = [pizza1 for pizza1 in friend_pizzas]
print(f"E as pizzas que meus amigos gostam são:{pizza_dos_amigos}")


