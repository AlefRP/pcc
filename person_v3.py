person = {
    'alef': [14, 13],
    'mohamed': [7, 879],
    'ahmed': [225, 18],
    'mohamed': [7, 879],
    'ahmed': [225, 18] 
}

# Looping a dict
for name, number in person.items():
    print(f"{name} favorite numbers are: ")
    for num in number:
        print(f"\t{num}")
        
# Loop to get names
for name in person.keys():
    print(name)