import os

os.system("clear")
def logoSenai():
    os.system("clear")
    print ("===== SENAI ====")

def preproduto():
    preco = float(input("Digite um numero"))
    inflaciona = preco *0.1
    inflaciona2 = preco * 0.2
    if preco < 100:
        preco = inflaciona + preco
    if preco >= 100:
        preco = inflaciona2 + preco
    print(f"O preço do produto e:{preco}")
logoSenai()
preproduto()