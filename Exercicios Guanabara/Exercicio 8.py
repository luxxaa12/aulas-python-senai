import os


os.system("clear")
#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

numero:int

numero = int(input("Digite um numero:"))

for i in range(1,11):
    print(f"{numero} * {i} = {numero * i}")
