import os

os.system("clear")
#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

numero: int
a: int
s: int


numero = int(input("Digite um valor:"))
a = numero - 1
s = numero + 1

print(f"O numero escolhido foi : {numero}")
print(f"O numero sucessor e : {s} ")
print(f"O numero antecessor e : {a}")