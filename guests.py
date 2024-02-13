guests = ['alef', 'gustavo', 'maria']
print(f"Hello {guests[0].title()}, I would like to invite you to dinner.")
print(f"Hello {guests[1].title()}, I would like to invite you to dinner.")
print(f"Hello {guests[2].title()}, I would like to invite you to dinner.")

wont_come ='gustavo'
guests.remove(wont_come)
guests.append('jose')

print(guests)
print(f"Hello {guests[0].title()}, I would like to invite you to dinner.")
print(f"Hello {guests[1].title()}, I would like to invite you to dinner.")
print(f"Hello {guests[2].title()}, I would like to invite you to dinner.")

guests.insert(0, 'pedro')
guests.insert(2, 'aline')
guests.append('carlos')

print(guests)

print(f"Hello {guests[0].title()}, I would like to invite you to dinner.")
print(f"Hello {guests[1].title()}, I would like to invite you to dinner.")
print(f"Hello {guests[2].title()}, I would like to invite you to dinner.")
print(f"Hello {guests[3].title()}, I would like to invite you to dinner.")
print(f"Hello {guests[4].title()}, I would like to invite you to dinner.")
print(f"Hello {guests[5].title()}, I would like to invite you to dinner.")

guest_1 = guests.pop()
guest_2 = guests.pop()
guest_3 = guests.pop()
guest_4 = guests.pop()

print(f"Sorry {guest_1.title()}, I can't invite you to dinner.")
print(f"Sorry {guest_2.title()}, I can't invite you to dinner.")
print(f"Sorry {guest_3.title()}, I can't invite you to dinner.")
print(f"Sorry {guest_4.title()}, I can't invite you to dinner.")

print(guests)

# Revoming with del
del guests[0]
del guests[0]

print(guests)
print(f"We have {len(guests)} people coming to dinner today.")