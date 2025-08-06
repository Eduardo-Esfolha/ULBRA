tarefas = [[ "beber agua", "acordar, levanta e ir toma agua", 5, 4]
]
tarefasok = []
resposta = 0

def menu() :
    global resposta
    while True:
        print("(1) adicionar")
        print("(2) editar")
        print("(3) ver tarefas")
        print("(4) concluir")
        print("(5) remover")
        print("(6) sair")

        resposta = int(input("digite a operação que quer fazer"))

        if resposta == 1 :
            adc()
        elif resposta == 2:
            edit()
        elif resposta == 3:
            visu()
        elif resposta == 4:
            ok()
        elif resposta == 5:
            remove()
        elif resposta == 6:
            exit()
        else:
            print("opção invalida")


def adc():
    nome = input("digite o nome da tarefa")
    disc = input("breve descrição da tarefa")
    rel = int(input("qual a relevancia da tarefas"))
    tempo = int(input("digite o tempo estimado para concluir"))

    tarefas.append([nome,disc,rel,tempo])
    print(tarefas)


def edit():
    print(tarefas)
    escolha = input("qual tarefa quer editar?(escreva o nome)")

    for tarefa in tarefas:
        if tarefa[0] == escolha:
            print("nome:", tarefa[0], "descriçao:", tarefa[1], "relevancia:", tarefa[2], "tempo estimado:", tarefa[3] )
            escolha2 = int(input("qual item da tarefa quer edita(1 para nome e 4 para tempo) e 5 para voltar ao menu"))
            if escolha2 == 1:
                novonome = input("qual o novo nome?")
                tarefa[0] = novonome
                print("nome alterado")
            elif escolha2 == 2:
                novodesc = input("qual a nova descrição?")
                tarefa[1] = novodesc
                print("descrição alterada")
            elif escolha2 == 3:
                novarel = int(input("qual a nova relevância?"))
                tarefa[2] = novarel
                print("relevância alterada")
            elif escolha2 == 4:
                novotempo = int(input("qual o novo tempo estimado?"))
                tarefa[3] = novotempo
                print("tempo estimado alterado")
            elif escolha2 ==5:
                menu()

def visu():
    print("(1) tarefas pendentes")
    print("(2) tarefas concluidas")

    escolha = int(input("quer visualizar quais tarefas?"))
    if escolha == 1:
     for i in tarefas:
            print("nome:", i[0])
            print("descriçao:", i[1])
            print("relevancia:", i[2])
            print("tempo estimado:", i[3])
    elif escolha == 2:
        for j in tarefasok:
            print("nome:", j[0])
            print("descriçao:", j[1])
            print("relevancia:",j[2])
            print("tempo estimado:", j[3])

def ok():
    print(tarefas)

    escolha = input("qual tarefa quer concluir? (digite o nome)")

    for i in tarefas:
        if i[0] == escolha:
            tarefasok.append(i)
            tarefas.remove(i)
            menu()

def remove():
    for i in tarefas:
        print("(1)", i[0])
    escolha = input("digite o numero da tarefa que quer excluir")
    for j in tarefas:
        if j[0] == escolha:
            tarefas.remove[j]



menu()


        

    



    



