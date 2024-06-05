from pathlib import Path

path = Path("text_files\learning_python.txt")

contents = path.read_text()

print(contents)

lines = contents.splitlines()

for line in contents.splitlines():
    print(line)

# for line in lines:
#     print(line)
    
for line in lines:
    print(line.replace("python", "C"))