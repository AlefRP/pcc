world_places = ["New York", "Paris", "Tokyo", "Dubai", "London"]
print(sorted(world_places))
print(world_places)

# Sorted in reverse alphabetical order
print(sorted(world_places, reverse=True))
print(world_places)

# Reversing the list
world_places.reverse()
print(world_places)

# Reversing the list again to get the original order
world_places.reverse()
print(world_places)

# Sort permanently alphabetically
world_places.sort()
print(world_places)

# Sort permanently in reverse alphabetical order
world_places.sort(reverse=True)
print(world_places)