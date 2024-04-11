import os

os.system("clear")
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real: float

real = float(input("Digite quantos reais voce quer converte em dolares:"))

print(f"US${real/5.09:.1f}")