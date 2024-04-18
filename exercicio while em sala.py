

#escreva um algoritmo que pergunte ao usuario se deseja inserir mais
#uma nota, se a resposta do usuario for "N", o programa fara a media
#aritimetica das notas informadas e mostrara a media aritmetica para
# o usuario.
# obs use um contador dentro do laço de repetiçao para contar a quantidade 
#de  iteraçoes(loops)

import os

os.system("clear")

nota : float = -1
soma : float =  0
contador = 0

while True:

      nota = float(input("Digite a Nota: "))
      soma += nota 
      contador += 1
    
      resposta = (input("Deseja inserir mais uma nota?"))
      
      if resposta != 's':
          break

media = soma / contador

print(f"Média: {media}")
print(contador)
print(soma )
