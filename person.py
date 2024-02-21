person = {
    'first_name': 'Alef',
    'last_name': 'Pereira',
    'age': 27,
    'city': 'Elói Mendes'
}

# Favorite number

person = {
    'alef': 7,
    'maria': 9,
    'joao': 10,
    'jose': 8,
    'ana': 6,
    'carlos': 5
}

glossary = {
    'string': 'a series of characters.',
    'comment': 'a note in a program that the Python interpreter ignores.',
    'list': 'a collection of items in a particular order.',
    'loop': 'work through a collection of items, one at a time.',
    'dictionary': "a collection of key-value pairs."
}

# print(f"String: {glossary['string']}")
# print(f"Comment: {glossary['comment']}")
# print(f"List: {glossary['list']}")
# print(f"Loop: {glossary['loop']}")
# print(f"Dictionary: {glossary['dictionary']}")

# Loop structure for interating in a dict, I can use any variable name for the key and value
for name, points in person.items():
    print(f"{name.title()}: {points}")
    
search_peaple = ['alef', 'maria', 'joao', 'bone', 'luffy']

# I can use any variable name for the key and value
for name in search_peaple:
    if name in person.keys():
        print(f"{name.title()}, thanks for your participation!")
    else:
        print(f"{name.title()}, you are not in the list. Would you like to join?")