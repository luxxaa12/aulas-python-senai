import os
os.system("clear")

# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

numero : float

numero = float(input("Digite um numero:"))

print(f"O Numero em km:{numero*1000}m")
print(f"O Numero em hectometro:{numero*100}m")
print(f"O Numero em decametros:{numero*10}m")
print(f"O Numero em metros:{numero}m")
print(f"O Numero em centimetros:{numero*0.1}m")
print(f"O Numero em decimetro:{numero*0.01}m")
print(f"O Numero em milimitro:{numero*0.001}m")

