current_users = ['admin', 'charles', 'martina', 'michael', 'florence', 'eli']

new_users = ['Charles', 'florence', 'abda', 'michael', 'admin']

for user in new_users:
    if user.lower() in current_users:
        print(f"Sorry, the username {user} is already taken.")
    else:
        print(f"Username {user} is available.")

numbers = [1, 2, 3, 4, 5]

# Ordinal numbers loop
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")