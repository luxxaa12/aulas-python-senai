import os

os.system("clear")
#Crie um programa que leia dois números e mostre a soma entre eles.

n1:int
n2:int
soma:int

n1 = int(input("Digite o numero equivalente ao primeiro numero:"))
n2 = int(input("Digite o numero equivalente ao segundo numero:"))

soma = n1 + n2

print(f"A soma entre :{n1} e {n2} e = {soma}")