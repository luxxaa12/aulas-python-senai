import os

os.system("clear")

numero: float = -1;

while numero < 0 or numero > 10:
    numero =float(input("Digite um numero"));
    os.system("clear")

print(f"numero informado:{numero}")
    