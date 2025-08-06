tupla = ("segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo")
print("1-segunda")
print("2-terça")
print("3-quarta")
print("4-quinta")
print("5-sexta")
print("6-sabado")
print("7-domingo")
semana = int (input("digite o numero correspondente ao dia que quer. 1 para segunda e 7 para domingo"))

if 1<= semana <=7:
    print(tupla[semana - 1])
else:
    print("erro")
