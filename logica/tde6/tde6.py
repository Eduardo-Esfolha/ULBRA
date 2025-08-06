numeros = int (input ("digite um numero com quatro digitos"))

milhar = (numeros //1000) 
centena = (numeros //100) % 10
dezena = (numeros //10) % 10 
unidade = numeros % 10

if numeros // 10000 == 0 and numeros > 999:
    maiorvalor = max (milhar, centena, dezena, unidade )
    print(f"maior valor é = {maiorvalor}")
    soma = milhar+centena+dezena+unidade
    print(f"a soma é = {soma}")

    if milhar!=centena and centena!=dezena and dezena!=unidade and unidade!=milhar and unidade!=centena and dezena!=milhar:
       print("nao há numeros repetidos ")
    else:
        print("ha numeros repetidos")

    if unidade == milhar and centena == dezena:
        print("o numero é palíndromo")
    else:
        print("o numero nao é  palíndromo")
else:
     print(" o numero não tem quatro digitos")