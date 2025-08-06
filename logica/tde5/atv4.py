nota =  int (input ("qual foi sua nota?"))

if nota >=6:
    prazo = input(("voce entregou dentro do prazo? (sim ou nao)")).strip().lower()=="sim"
    ap = input(("apresentou ele? (sim ou nao)")).strip().lower()=="sim"
if prazo == True and ap == True:
    print("voce foi aprovado")

else:
    print ("reprovado")