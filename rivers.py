rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

# Loop of dict rivers
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
    
for river in rivers:
    print(river)

# The same as before   
for river in rivers.keys():
    print(river)
    
for country in rivers.values():
    print(country)