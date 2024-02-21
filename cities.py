cities = {
    'Boston': {
        'country': 'United States',
        'population': 645000,
        'fact': 'home of the Boston Celtics',
    },
    'Paris': {
        'country': 'France',
        'population': 2200000
    },
    'London': {
        'country': 'England',
        'population': 850000,
        'fact': 'home of the London Underground'
    }
}

# Looping a dict of dicts
for city in cities:
    print(f"\n{city}")
    for item, info in cities[city].items():
        print(f"\t{item}: {info}")