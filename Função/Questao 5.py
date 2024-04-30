import os 

os.system("clear")

def logoSenai ():
    os.system("clear")
    print("====Senai ====")
    
def metpcm():
    valor = int(input("Digite um valor para converter em cm:"))
    valor = valor * 100

    print(f"O numero convertido em centimetros e : {valor}")

metpcm()