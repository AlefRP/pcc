toppinfs = []

while True:
    topping = input("Enter a topping or 'quit' to end: ")
    if topping == 'quit':
        break
    else:
        toppinfs.append(topping)
        
print(toppinfs)