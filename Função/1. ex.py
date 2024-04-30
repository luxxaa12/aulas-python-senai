import os

os.system("clear")

#Funçao retorno

def logoSenai():
    os.system("clear")
    print ("===== SENAI ====")
    print("Solte minha camisa")
#Solicitando dados do usuario.

logoSenai()
nome = str(input("Digite seu nome:"))

logoSenai()
idade = int(input("Digite sua idade:"))

logoSenai()
peso= float(input("Digite seu peso:"))

#Exibindo dados para o usuario
logoSenai()
print(f"Nome:{nome}")
print(f"idade: {idade}")
print(f"peso : {peso:.2f}")