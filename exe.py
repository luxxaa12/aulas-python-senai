import os

os.system("clear")

QTDNUMEROS = 5
contador = 0
mediageral = 0 
somageral = 0
mediapares = 0 
somapares = 0
contadorpositivo = 0
contadornegativo = 0
mediaimpares = 0
somaimpares = 0
qtdpares = 0
qtdimpares = 0
qtdpositivo = 0
qtdnegativo = 0
maiornumero = 0
menornumero =9999
contadorpar = 0 
contadorimpar = 0
num = []
numeros =0
contadorgeral=0

for i in range (QTDNUMEROS):
    
    contadorgeral +=1
    numero = int(input("Digite um numero:"))
    somageral += numero

    num.append(numero)

    if numeros > 0:
        qtdpositivo += 1
        contadorpositivo +=1
    if numeros < 0:
        qtdnegativo +=1
        contadornegativo +=1
    if numeros  %2 == 0:
        qtdpares += 1
        somapares += num[i]
        contadorpar += 1
    else:
        qtdimpares += 1
        somaimpares += num[i]
        contadorimpar += 1
    if numeros > maiornumero:
        maiornumero = num[i]
    if numeros > menornumero:
        menornumero = num[i]

mediapares = somapares/contadorpar
mediaimpares = somaimpares/qtdimpares
mediageral = somageral / contadorgeral
    
print(f"A quantidade de valores apresentados e : {QTDNUMEROS}")
print(f"A quantidade de valores positivos e : {qtdpositivo}")
print(f"A quantidade de valores negativos e : {qtdnegativo}")
print(f"A quantidade de valores pares e : {qtdpares}")
print(f"A quantidade de valores impares e : {qtdimpares}")
print(f"A media de valores pares e : {mediapares}")
print(f"A media de valores impares e : {mediapares}")
print(f"A media geral e : {mediageral}")
print(f"O maior numero e : {maiornumero}")
print(f"O menor numero e : {menornumero}")

