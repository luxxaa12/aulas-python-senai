#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

import os

os.system("clear")

Pproduto =  float(input("Digite o preço de um produto:"))
print("O PREÇO DO PRODUTO SOFRERA UM DESCONTO DE 5%\n")

desconto = Pproduto*0.05

print(f"O preço do produto com o desconto e de :R${Pproduto - desconto}")

