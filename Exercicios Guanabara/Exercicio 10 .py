#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

import os

os.system("clear")


altura = float(input("Digite uma altura:"))
largura = float(input("Digite uma largura:"))

area = largura*altura

print(f"A area da parede foi: {area} quadrados")
print(f"A quantidade de tinta necessaria e: {area/2} litros")