
active = True
while active:
    age = int(input("How old are you? "))
    
    if age < 0:
        print("Age cannot be negative.")
        continue
    
    if age < 3:
        print("Your ticket is free.")
    elif age < 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")
    
    active = False
    