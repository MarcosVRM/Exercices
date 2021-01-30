# codigo do exercico
#usuario = input("Informe o usuário do sistema!")
#
#if(usuario == "Flávio"):
#    print("Seja bem-vindo Flávio!")
#else(usuario == "Douglas"):
#    print("Seja bem-vindo Douglas!")
#else(usuario == "Nico"):
#    print("Seja bem-vindo Nico")
#else:
#    print("Usuário não identificado!")
#minha correção
usuario = (input('Informa o usuário do sistema! :'))
usuario = usuario.capitalize()
print(usuario)
user1 = ["Flávio", "Flavio"]
user2 = "Douglas"
user3 = "Nico"

if(usuario in user1):
    print('Bem-vindo Flávio!')
else:
    if(user2 == usuario):
        print("Bem-vindo Douglas!")
    elif(user3 == usuario):
        print('Bem-vindo Nico!')
    else:
        print('Usuario invalido')
