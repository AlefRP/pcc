favorite_places = {
    'alef': ['paris', 'rome', 'london'],
    'beth': ['paris', 'rome'],
    'gimel': ['paris', 'rome', 'london'],
    'alex': ['usa', 'canada']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")