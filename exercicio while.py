import os

os.system("clear")

soma :float
media:float

numero1 =-1
numero2 =-1

while numero1 < 0 or numero1 > 10:
    numero1= float(input("Digite uma nota1:"))


while numero2 < 0 or numero2 > 10:
    numero2 = float(input("Digite uma nota2:"))

soma = numero1 + numero2
media = soma/2

print(f"A media do aluno foi :{media}")