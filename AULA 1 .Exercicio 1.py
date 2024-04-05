import os

os.system("clear")

nome : str
n1 : float
n2 : float
n3:  float
n4: float
soma: float
media : float

idade : int
media : float


nome = str(input("Digite seu nome"))
n1 = float(input("Digite sua nota"))
n2 = float(input("Digite sua nota"))
n3 = float(input("Digite sua nota"))
n4 = float(input("Digite sua nota"))

idade = int(input("Digite sua idade"))

soma = n1+n2+n3+n4
media = soma/4

os.system("clear")

print(f"Nome  : {nome}")
print(f"idade : {idade}")
print(f"Media : {media}")
