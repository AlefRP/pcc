alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points']) # error

# Defing standard return for a value not present at the dictionary
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)