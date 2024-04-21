#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

import os

os.system("clear")

GrausC=float(input("Digite um valor em graus:"))

GpF = GrausC * 1.8 + 32

print(f"o valor de graus celsiu para faranheit e:{GpF}")