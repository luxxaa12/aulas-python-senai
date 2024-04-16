import os

os.system("clear")


numero = int(input("Digite o numero que deseja ver a tabuada:"))

for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")