import random

dificuldade = input("Dificuldade 1 - DIFÍCIL (1 tentativa) | 2 - NORMAL (3 tentativas) | 3 - FÁCIL (5 tentativas)")
dificuldade = int(dificuldade)
numeroAleatorio = random.randrange(11)

#print(numeroAleatorio)

if dificuldade == 3:
    tentativas = 5
if dificuldade == 2:
    tentativas = 3
if dificuldade == 1:
    tentativas = 1

while tentativas != 0:
    tentativas = tentativas - 1 
    tentativaUsuario = input("Qual foi o número sorteado?")
    tentativaUsuario = int(tentativaUsuario)
    if tentativas == 0: 
        print("Acabou suas tentativas, tente novamente")
    if tentativaUsuario == numeroAleatorio: 
        print("VOCÊ ACERTOU!!!")
        break

    
    

