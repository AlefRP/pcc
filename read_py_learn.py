from pathlib import Path

path = Path("text_files\learning_python.txt")
contents = path.read_text().rstrip()

# print(contents)

# lines = contents.splitlines()

for line in contents.splitlines():
    print(line.replace("python", "C").rstrip())
