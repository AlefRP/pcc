favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust'],
    'phil': ['python', 'rust'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is: {languages[0].title()}")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
            
    # print(f"\n{name.title()}'s favorite languages are:")
    # for language in languages: # languages here is the list from the dict - langagues will ne the item from each key
    #     print(f"\t{language.title()}")