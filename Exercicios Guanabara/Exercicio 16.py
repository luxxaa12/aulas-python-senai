#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import os

os.system("clear")

Coposto = float(input("Digite o valor do cateto oposto:"))
Cadjacente = float(input("Digite o valor do cateto adjacente:"))


hipotenusa = (Coposto ** 2 + Cadjacente ** 2) ** (1/2)

# O numero elevado a 2 e = **2
# A raiz quadrada de um numero e = **(1/2)
print(f"O valor da hipotenusa e :{hipotenusa:.2f}")
