from rest import Restaurant

restaurante = Restaurant("The Pizza Palace", "Pizza")
restaurante.describe_restaurant()

restaurante_places = input("How many places do you want to sit? ")
restaurante_places = int(restaurante_places)

if restaurante_places < 8:
    print("You can sit now!")
else:
    print(f"You will need to wait for {restaurante_places} tables.")