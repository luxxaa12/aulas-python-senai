import os
os.system("clear")

def mediar(n1,n2):
    resultado = n1+n2/2
    return resultado

def situaçao(resultado):

    if resultado >= 7:
        print("o aluno esta aprovado:")
    else :
        print(" o aluno esta reprovado:")    

primeironumero = float(input("Digite a primeira nota:"))
segundonumero = float(input("Digite a segunda nota:"))

media = mediar(primeironumero,segundonumero)

print(f"A media ")
