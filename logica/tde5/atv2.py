ld1 = float(input ("digite o valor do lado 1"))
ld2 = float(input("digite o valor do lado 2"))
ld3 = float(input("digite o valor do lado 3"))

if ld1+ld2>ld3 and ld2+ld3>ld1 and ld3+ld1>ld2:
    if ld1==ld2==ld3:
        print("equilatero")
    elif ld1==ld2 or ld2==ld3 or ld1==ld3:
     print("isosceles")
    else:
     print("escaleno")
else:
    print("nao é um triangulo")