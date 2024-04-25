#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
import os

os.system("clear")

angulo = float(input("Digite o valor do angulo:"))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f"O seno do angulo e : {seno:.2f}")
print(f"O cosseno do angulo e : {cosseno:.2f}")
print(f"A tangente do angulo e : {tangente:.2f}")