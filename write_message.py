from pathlib import Path

path = Path("text_files\programing.txt")
# path.write_text("I love Python")

contents = "I love programming in Python!\n"
contents += "I love creating games!\n"
contents += "I love working with data!\n"

path.write_text(contents)