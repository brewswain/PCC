pizzas = ['hawaiian', 'pepperoni', 'meat lovers']
friend_pizzas = pizzas[:]

pizzas.append('veggie')
friend_pizzas.append('cheese')

print('My favourite pizzas are:')
for pizza in pizzas:
    print(pizza.title())


print("\nMy friend's favourite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())
