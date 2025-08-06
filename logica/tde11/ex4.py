lista = ["maça", "banana", "laranja", "uva", "abacaxi"]

def remove_item():
    print("Lista atual:", lista)
    remove= input("digite o item que deseja remover de 0 para banana a 5 abacaxi: ")
    if remove in lista:
        lista.pop(remove)
        print("item", remove, "removido com sucesso!")
        print("Lista atualizada:", lista)
    else:
        print("item não encontrado")

remove_item()