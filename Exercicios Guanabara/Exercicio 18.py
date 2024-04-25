#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
# que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
import os

os.system("clear")

nome:str

for nome in range (0,4):
    nome =input("Digite um nome :")

escolhido = random.choice(nome1,nome2,nome3,nome4)

print(f"O ALUNO ESCOLHIDO FOI :{escolhido}")