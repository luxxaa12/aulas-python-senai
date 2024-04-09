import os

os.system("clear")
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input("Digite algo:")
print("O tipo primitivo desse valor e",type(a))
print("So tem espaço?",a.isspace())
print("E numero?",a.isnumeric())
print("E alfabetico?",a.isalpha())
print("E alfanumerico",a.isalpha())
print("Esta em MAIUSCULO",a.isupper())
print("Esta em minusculo",a.islower())
print("Esta capitalizada",a.istitle())