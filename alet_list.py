things = ["mozzarella", "cinderella", "salmonella"]

print(things[1])
print(sorted(things))
print(things)
print(things[2].upper())

print(sorted(things, reverse=True))

things.sort(reverse=True)
things.sort()

things.reverse()

# I can use range inside list to create a list of numbers - 1 to 5
numbers = list(range(1, 6))
print(numbers)