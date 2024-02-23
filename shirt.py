def make_shirt(size='large', text='I love Python'):
    """
    Prints a message about the size of the shirt
    """
    if size == 'large' and text == 'I love Python':
        print(f"{text}!")
    else:
        print(f"{text} {size}")
    
make_shirt('large', 'My shirt is')
make_shirt(size='medium', text='My shirt is')

make_shirt()

def describe_city(city, country='USA'):
    """
    Prints a message about a city and its country
    """
    print(f"{city} is in {country}")
    
describe_city('Reykijavik', 'Iceland')
describe_city('New York')
describe_city('London', 'England')
    
