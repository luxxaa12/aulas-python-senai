import os

os.system("clear")

#funçao sem retorno
def logoSenai ():
    os.system("clear")
    print("====Senai ====")

#funçao cpm retorno
def somar(n1,n2):
    resultado = n1 + n2
    return resultado

logoSenai()
primeironumero = int(input("Digite um numero:"))
segundonumero = int(input("Digite um numero:"))

soma = somar(primeironumero,segundonumero)

print(f"Soma: {soma}")
