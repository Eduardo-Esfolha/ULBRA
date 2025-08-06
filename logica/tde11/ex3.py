lista = ["maça", "banana", "laranja", "uva", "abacaxi"]

def add_item():
    item = input("digite o item que deseja adicionar: ")
    lista.append(item)
    print("item", item, "adicionado com sucesso!")
add_item()
print("Lista atualizada:", lista)