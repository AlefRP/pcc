from pathlib import Path

path = Path("text_files\guest.txt")

message = input("What is your name? ")

path.write_text(message)