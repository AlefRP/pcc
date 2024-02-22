# Começa com usuários que precisam ser verificados
# e uma lista vazia para armazenar os confirmados

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Faz verificação de cada usuário até que não tenha mais ninguém para verificar
while unconfirmed_users:
    current_user = unconfirmed_users.pop() # Remove da lista anterior e armazena em uma variável

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Exibe usuarios confirmados
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())