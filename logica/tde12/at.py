estoque = [
         ]

resposta = 0

def adc():
     nome = input(("digite o nome do produto"))
     qtd = int (input(("digite a quantidade")))
     prc = float (input (("digite o preço do produto")))

     estoque.append([nome, qtd, prc])
     print(estoque)
     menu()
    

def listar():
    for linha in estoque:
        for produto in linha:
            print(produto, end=" ")
        print()
    menu()


def remover():
    nome = input("digite o nome do produto que deseja remover: ")
    for i in estoque:
        for j in i:
            if j == nome:
                estoque.remove(i)
                print((nome)+"removido com sucesso!")
                menu()  


    
def menu():
    global resposta
    while True:
        print("Menu de Estoque")
        print("1 adicionar")
        print("2 remover")
        print("3 listar")
        print("4 preço")
        print("5 sair")
        resposta = int (input("digite o numero da opção que deseja"))
        if resposta == 1:
            adc()
        elif resposta == 2:
            remover()
        elif resposta == 3:
            listar()
        elif resposta == 4:
            preco()
        elif resposta == 5:
            print("saindo...")
            exit()
        else:
            print("opção inválida")
            menu()



menu() 




   # nome = input(("digite o nome do produto"))
    #qtd = int (input(("digite a quantidade")))
   # prc = float (input (("digite o preço do produto")))