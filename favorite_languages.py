favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# Loop structure for interating in a dict, I can use any variable name for the key and value
for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {languages.title()}.")

# Print just the keys of a dict
for name in favorite_languages.keys():
    print(name.title())
    
# This also works to print the keys
for name in favorite_languages:
    print(name.title())

# Print favorite name of friends
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        # Using key notation to get the value
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
    
    # Using keys() method to check if a key is in a dict - not only used for loops
    if 'erin' not in favorite_languages.keys():
        print("Erin, please take our poll!")
        
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
    
print("The following languages have been mentioned:")

# Loop to print values of dict using values method
for language in favorite_languages.values():
    print(language.title())
    
# Loop to print values of dict using set - a set get just unique values
for language in set(favorite_languages.values()):
    print(language.title())