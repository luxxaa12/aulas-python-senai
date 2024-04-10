import os

os.system("clear")

#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input("Digite a nota 1 :"))
n2 = float(input("Digite a nota 2 :"))
soma = n1+n2
media = soma / 2

print(f"A media do aluno foi: {media}")
