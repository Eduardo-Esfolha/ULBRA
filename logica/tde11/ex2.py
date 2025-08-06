lista = ["maça", "banana", "laranja", "uva", "abacaxi"]

item = input("digite o item que deseja procurar: ")

for i in lista:
    if i == item:
        print("item encontrado")
        break
    else:
        print("item não encontrado")
        break
