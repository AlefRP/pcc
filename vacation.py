prompt_name = "Whats your name? "
prompt = "\nIf you could travel anywhere, where would you go? "

travels = {}

##############################################################
### To modify lists or dicts its better to use while loops ###
##############################################################

# Add responses until the user says no
while True:
    name = input(prompt_name)
    reponse = input(prompt)
    
    travels[name] = reponse
    
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat != "yes":
        break

# Print dicts itens and keys 
for name, reponse in travels.items():
    print(f"{name.title()} would like to go to {reponse.title()}.")