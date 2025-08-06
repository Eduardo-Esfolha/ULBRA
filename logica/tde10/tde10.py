login = "inter"
password = "1009"
contador = 0 
alterar = 0
nome =""
idade = 0
email = ""
def logar():
    global login
    global password
    global contador
    global menu
    print("bem-vindo ao sistema de login")
    while True:
        valor1 = input("digite seu usuario")
        valor2 = input("digite sua senha")
        if valor1 == login and valor2 == password:
            menu()
        else :
            print("usuario ou senha incorretos")
            contador += 1
            if contador == 3:
                print("tente mais tarde")
                break
            else:
                print("voce ainda tem", 3-contador, "tentativas")
                continue

def menu():
    global nome
    global idade
    global email
    global contador
    print("ola, bem vindo", login)
    print("1- cadastrar info")
    print("2- editar")
    print("3- quantas tenativas de login")
    print("4- exibir perfil")
    print("5- sair")
    while True:
        opcao = int(input("digite a opcao desejada"))
        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            editar()
        elif opcao == 3:
            print("foram erradas", contador, "tentativas de login")
        elif opcao == 4:
            print("seu nome é", nome)
            print("sua idade é", idade)
            print("seu email é", email)
            menu()
        elif opcao == 5:
            break
        else:
            print("opcao invalida")
    
def cadastrar():
    global nome
    global idade    
    global email
    print("cadastrar")
    nome = input("digite seu nome")
    idade = int(input("digite sua idade"))
    email = input("digite seu email")
    print("cadastrado com sucesso")
    menu()

def editar():
    global login
    global password
    global contador
    global alterar
    print("alterando dados")

    while True:
        confirmaçao = input("voce quer alterar usario, senha ou ambos? (u/s/a)")
        if confirmaçao == "u":
            login = input("digite seu novo usuario")
            alterar += 1
            print("usuario alterado com sucesso")
            menu()
        elif confirmaçao == "s":
            password = input("digite sua nova senha")
            alterar += 1
            print("senha alterada com sucesso")
            menu
        elif confirmaçao == "a":
            login = input("digite seu novo usuario")
            password = input("digite sua nova senha")
            print("usuario e senha alterados com sucesso")
            alterar += 2
            menu()
        else:
            print("opcao invalida")
            continue
            
            
logar()