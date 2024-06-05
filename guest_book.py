from pathlib import Path

path = Path("text_files\guest_book.txt")

contents = ''

while True:
    name = input("What is your name? ")
    if name == "quit":
        break
    contents += f"{name}\n"

path.write_text(contents)