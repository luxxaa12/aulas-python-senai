#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import os

os.system("clear")

Real = float(input("Digite um numero real:"))

print(f"A porção inteira desse numero real e : {Real:.0f}")


