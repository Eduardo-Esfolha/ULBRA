
estoque = 5
vendas = 0 
repo = 0
resposta =0
quantidade = 0

def vender():
    global estoque, vendas
    while True:
        quantidade = int(input("digite quantas vendas quer fazer ou se quiser sair escreva 0"))
        if quantidade == 0:
            break
        try:
            if quantidade > estoque:
                estoque-= quantidade
                vendas+= quantidade
                break
        except ValueError:
            print("estoque insuficiente")
            
while True:
    resposta = int(input("vender(1)" \
    "repor(2)" \
    "3(consultar)" \
    "4(encerrar)"))

    if resposta == 1:
            resposta = vender()
    elif resposta ==2 :
        quantidade = int(input("quantas repo"))
        estoque+= quantidade
        vendas+= quantidade
    elif resposta ==3:
        print(estoque)
    elif resposta == 4:
        print("foram feitas", vendas, "vendas")
        print("foram feitas", repo, "reposição")
        break
    else:
        print("opção invalida")