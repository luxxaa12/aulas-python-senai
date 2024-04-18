import os

os.system("clear")

nota =-1
soma:float = 0

for i in range(1,4):
    while True :
        nota= float(input("Digite a nota"))
        if nota <0 or nota >10:
         print("nota invalida")
        else:
           soma += nota
           break;
            
    media = soma / 3 

    print(f"A media do aluno foi: {media}")
    
    if media >= 7:
       print("O aluno esta aprovado")

    elif media >= 5:
       print("O aluno esta de recuperaçao")

    else :
        print("O aluno esta reprovado")  
