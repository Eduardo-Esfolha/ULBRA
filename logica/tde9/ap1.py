
def validar(resposta):
    while True:
        try:
            resposta = int(input(resposta))
            if 1 <= resposta <=5:
                return resposta
            else:
                print("digite um valor entre 1 e 5")
        except ValueError:
            print("digite um valor entre 1 e 5")


print("hoje iremos ver qual area voce tem afinidade, respondendo as perguntas com numeros de 1 a 5")
print("reposta primeiro as perguntas sobre desenvolvimento de software")
dev1 = validar (("Gosto de programar e resolver problemas com código."))
dev2 = validar (("Tenho interesse em criar aplicativos e sites."))
dev3 = validar (("Gosto de aprender novas linguagens de programação."))
dev4 = validar(("Prefiro trabalhar com lógica e estruturação de código."))
dev5 = validar (("Tenho paciência para depurar erros e otimizar código."))
resultdev = dev1+dev2+dev3+dev4+dev5

print("responda agora as pergunta sonre a area de produto")
prod1 = validar (("Gosto de pensar na experiência do usuário ao usar um sistema."))
prod2 = validar (("Tenho interesse em pesquisa de mercado e comportamento do usuário."))
prod3 = validar (("Me interesso por criar soluções inovadoras e intuitivas."))
prod4 = validar (("Gosto de trabalhar com design, wireframes ou prototipagem."))
prod5 = validar (("Quero entender e definir estratégias para melhorar produtos digitais."))
resultprod = prod1+prod2+prod3+prod4+prod5

print("responda agora sobre a area de qualidade")
qua1 = validar (("Gosto de testar e garantir que sistemas funcionem corretamente."))
qua2 = validar (("Tenho interesse em encontrar erros e melhorar a estabilidade dos produtos."))
qua3 = validar (("Acredito que testes automatizados ajudam a evitar falhas em sistemas."))
qua4 = validar (("Gosto de seguir padrões e documentar processos para garantir qualidade."))
qua5 = validar (("Quero trabalhar garantindo que um software funcione bem para todos os usuários."))
resultqua = qua1+qua2+qua3+qua4+qua5

if resultdev > resultprod and resultdev > resultqua:
    print("mais afinilidade com desenvolvimento")
elif resultprod > resultdev and resultprod > resultqua:
    print("mais afinilidade com produçao")
elif resultqua > resultprod and resultqua > resultdev:
    print("mais afinidade com qualidade")
elif resultdev == resultprod and resultdev > resultqua :
    print("voce tem afinidade com desenvolvimento e produção")
elif resultdev == resultqua and resultdev > resultprod:
    print("voce tem afinidade com desenvolvimento e qualidade")
elif resultprod  == resultqua and resultprod > resultdev:
    print("voce tem afinidade com produçao e qualidade")
else:
    print("voce tem afinidades com todas")