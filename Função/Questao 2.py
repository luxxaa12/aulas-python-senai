import os

os.system("clear")

def tabuada():
    numero = int(input("Digite um numero:"))
    
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")
    

tabuada()