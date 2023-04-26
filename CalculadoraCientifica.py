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
    tipo_operacao = int(input("O número que você vai passar é? \n 1 -> DECIMAL \n 2 -> HEXADECIMAL \n 3 -> OCTAL \n 4 -> BINÁRIO \n"))
    
    def operacao(tipo_operacao):
        # DECIMAL -> HEXADECIMAL / OCTAL / BINÁRIO
        if tipo_operacao == 1:
            numero = input("Digite o número decimal:")
            decimalParabinario(numero)
            decimalParahexadecimal(numero)
            decimalParaoctal(numero)
        # HEXADECIMAL -> DECIMAL / OCTAL / BINÁRIO
        if tipo_operacao == 2:
            numero = input("Digite o número HexaDecimal:")
            HexaDecimalParaDecimal(numero)
        
        # OCTAL -> DECIMAL / HEXADECIMAL / BINÁRIO
        if tipo_operacao == 3:
            numero = input("Digite o número OCTAL:")
            octalParaDecimal(numero)

        # BINÁRIO -> DECIMAL / HEXADECIMAL / OCTAL
        if tipo_operacao == 4:
            numero = input("Digite o número BINÁRIO:")
            binarioParaDecimal(numero)
    
    def decimalParahexadecimal(numero):
        hexadecimal = hex(int(numero)).upper()

        print("Este número em HexaDecimal é:", hexadecimal[2:])

    def decimalParaoctal(numero):
        octal = oct(int(numero))

        print("Este número em octal é:", octal[2:])

    def decimalParabinario(numero):
        binario = bin(int(numero))

        print("Este número em binario é:", binario[2:])


    def HexaDecimalParaDecimal(numero):
        decimando = int(numero, 16)
    
        print("Este número em decimal é:", decimando)
        
        decimalParaoctal(decimando)
        decimalParabinario(decimando)

    def octalParaDecimal(numero):
        octando = int(numero, 8)

        print("Este número em decimal é:", octando)

        decimalParabinario(octando)
        decimalParahexadecimal(octando)

    def binarioParaDecimal(numero):
        binariando = int(numero, 2)
        print("Este número em decimal é:", binariando)

        decimalParahexadecimal(binariando)
        decimalParaoctal(binariando)


        

    operacao(tipo_operacao)
Programador()
        