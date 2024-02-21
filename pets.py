pets = [
    {
        'breed': 'Husky',
        'name': 'Fido',
        'age': 5,
        'owner': 'John Smith'
    },
    {
        'breed': 'Beagle',
        'name': 'Rex',
        'age': 3,
        'owner': 'Jane Doe'
    },
    {
        'breed': 'Poodle',
        'name': 'Lucy',
        'age': 2,
        'owner': 'Bob Smith'
    }
]

# Interating about the list of dicts another way
for pet in pets:
    print(f"{pet['name']} is a {pet['breed']} and is {pet['age']} years old.")
    print(f"{pet['name']}'s owner is {pet['owner']}.")