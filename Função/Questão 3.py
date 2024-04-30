import os

os.system("clear")

def logoSenai():
    os.system("clear")
    print("====Senai====")

def somar(n1,n2):
    resultadosoma = n1 + n2
    return resultadosoma

def subtracao(n1,n2):
    resultadosub = n1 - n2
    return resultadosub

def multiplicacao(n1,n2):
    resultadomult = n1 * n2
    return resultadomult
def divisao(n1,n2):
    resultadodivi = n1 /n2
    return resultadodivi
    
logoSenai()
primeironumero = int(input("Digite um numero:"))
segundonumero = int(input("Digite um numero:"))

mult = multiplicacao(primeironumero,segundonumero)
som = somar(primeironumero,segundonumero)
sub = subtracao(primeironumero,segundonumero)
div = divisao(primeironumero,segundonumero)

logoSenai()
print(f"A soma e : {som}")
print(f"A multiplicacao e :{mult}")
print(f"a subtraçao e : {sub}")
print(f"a divisao e :{div}")