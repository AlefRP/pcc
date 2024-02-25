def city_country(city, country):
    """Return a city-country pair"""
    return f"{city.title()}, {country.title()}"

print(city_country('Nova York', 'USA'))
print(city_country('paris', 'france'))
print(city_country('london', 'england'))