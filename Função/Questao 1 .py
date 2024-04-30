import os

os.system("clear")
def logoSenai():
    os.system("clear")
    print("====SENAI====")

def somar (n1,n2):
    resultado= n1 + n2
    return resultado

def mediar(resultado):
    resultadomed = resultado / 2
    return resultadomed

logoSenai()
primeironumero= int(input("Digite o primeiro numero:"))
segundonumero= int(input("Digite o primeiro numero:"))

soma = somar(primeironumero,segundonumero)
media = mediar(soma) 

print(f"a media dos numeros e :{media}")
