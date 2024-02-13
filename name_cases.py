name = "Alef"
print(f"Olá {name}, gostaria de aprender um pouco de Pyhton hoje?")

# Lowercase
print(name.lower())

# Uppercase
print(name.upper())

# Title
print(name.title())

citation = "Albert Einstein once said, \"A person who never made a mistake never tried anything new.\""
print(citation)

famous_person = "Albert Einstein"
citation = f"{famous_person} once said, \"A person who never made a mistake never tried anything new.\""
print(citation)


name = "\tAlef\n"

# Remove white space from left side of the string
print(name.lstrip())

# Remove white  space from right side of the string
print(name.rstrip())

# Remove white space from both sides of the string
print(name.strip())

file_name = "programming.txt"
print(file_name.removesuffix(".txt"))