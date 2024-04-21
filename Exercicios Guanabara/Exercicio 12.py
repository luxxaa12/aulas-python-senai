#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

import os

os.system("clear")

salario = float(input("Digite seu salario:"))

aumento = salario*0.15

print(f"\nO salario com aumento e : {salario + aumento}")