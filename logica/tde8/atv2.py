resposta = 0
gasolina = 0
alcol = 0
tanque = 0
while resposta != 3:
    resposta = int (input("voce quer abastecer o que hoje?" \
    "1(gasolina)" \
    "2(alcol)" \
    "3(sair)"))

    if resposta == 1 :
        combustivel = int (input ("quantos litros?"))
        while tanque <= combustivel:
            print ("abastecendo", tanque)
            tanque +=1
            
    elif resposta == 2 :
        combustivel = int (input ("quantos litros?"))
        while tanque <= combustivel:
            print ("abastecendo", tanque)
            tanque +=1
    elif resposta == 3:
        print("obrigado e boa noite")

    else:
        print("valor invalido")

