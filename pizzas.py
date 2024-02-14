pizzas = ["peperoni", "mussarela", "calabresa"]
for pizza in pizzas:
    print(f"I like {pizza} pizza")

print("I really love pizza!")

friend_pizzas = pizzas[:]

pizzas.append("4 queijos")
friend_pizzas.append("portuguesa")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)