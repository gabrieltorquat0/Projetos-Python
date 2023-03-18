
#Função da calculadora padrão
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

#Função da calculadora de programador
def Programador():
    operação = int(input("O número que você vai passar é? \n 1 -> DECIMAL \n 2 -> HEXADECIMAL \n 3 -> OCTAL \n 4 -> BINÁRIO \n"))
    numero = int(input("Qual é o número? "))

    #Operação 1 transformando decimal em hexadecimal
    if operação == 1:
        hexadecimal = []
        
        while numero >= 1:
            hexando = numero % 16
            numero = int(numero / 16)
        
            if hexando >= 0 and hexando <= 9: 
                hexadecimal.append(hexando)
            if hexando == 10:
                hexadecimal.append("A")
            if hexando == 11:
                hexadecimal.append("B") 
            if hexando == 12:
                hexadecimal.append("C")
            if hexando == 13:
                hexadecimal.append("D")
            if hexando == 14:
                hexadecimal.append("E")
            if hexando == 15:
                hexadecimal.append("F")

        hexadecimal.reverse()
        print(hexadecimal)
            
    




Programador()
    