people_1 = {
    'alef': 11,
    'beni': 12,
    'carmen': 13
}

people_2 = {
    'daniel': 14,
    'eli': 15,
    'fabio': 16
}

people = [people_1, people_2]

# Interating about the list of dicts
for person in people:
    for name, age in person.items():
        print(f'{name} is {age} years old')