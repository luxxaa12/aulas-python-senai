import os

os.system("clear")
#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

dobro :int
triplo: int
raizq : int

numero = int(input("Digite um numero:"))

dobro = numero * 2
triplo = numero * 3
raizq = numero * numero

print(f"O numero escolhido foi : {numero}")
print(f"O dobro do numero escolhido e : {dobro}")
print(f"O triplo do numero esolhido e : {triplo}")
print(f"A  raiz quadrada do numero escolhido e: {raizq}")
