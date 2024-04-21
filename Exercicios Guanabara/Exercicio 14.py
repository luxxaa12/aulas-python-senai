#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de
#dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

import os

os.system("clear")

QtdKm = float(input("Digite a quantidade de km rodados do carro alugado:"))
QtdDias = int(input("Digite quantos dias o carro foi alugado:"))

PQtdKm = QtdKm *0.15
PQtdDias =QtdDias * 60

print(f"O preço a pagar pelos km rodados e: R${PQtdKm}")
print(f"O preço a pagar pelos dias de aluguel e:R${PQtdDias}")
print(f"O total a pagar e : {PQtdDias + PQtdKm}")