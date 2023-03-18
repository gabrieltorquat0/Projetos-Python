


def Padrao():
    operação = int(input("Qual operação você quer fazer? \n 1 -> + | 2 -> - | 3 -> x | 4 -> / \n"))
    primeiroNumero = int(input("Digite o primeiro número da operação"))
    segundoNumero = int(input("Digite o segundo número"))

    if operação == 1:
        print (primeiroNumero + segundoNumero)
    elif operação == 2:
        print (primeiroNumero - segundoNumero)
    elif operação == 3:
        print (primeiroNumero * segundoNumero)
    elif operação == 4:
        print (primeiroNumero / segundoNumero)

def Programador():
    operação = int(input("O número que você vai passar é? \n 1 -> DECIMAL \n 2 -> HEXADECIMAL \n 3 -> OCTAL \n 4 -> BINÁRIO \n"))
    numero = int(input("Qual é o número? "))

    if operação == 1:
        hexadecimal = []

        #Transformando decimal em hexadecimal
        while numero >= 1:
            hexando = numero % 16
            numero = int(numero / 16)
            hexadecimal.append(hexando) 
        if hexadecimal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32] == 10:
            hexadecimal[] = "A"
        
        hexadecimal.reverse()
            

    print(hexadecimal)
            
    




Programador()
    