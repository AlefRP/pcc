from pathlib import Path

path = Path("text_files\pi_million_digits.txt")
contents = path.read_text().rstrip()

# print(contents)

lines = contents.splitlines()

# for line in lines:
#     print(line.rstrip())

pi_string = ''

for line in lines:
    pi_string += line.lstrip()
    
print(f"{pi_string[:52]}...") # print first 52 digits of pi_string
print(len(pi_string))