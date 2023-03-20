
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
    numero = input("Qual é o número? ")

    #Operação 1: Transformando numeros decimais
    if operação == 1:
        def hexadecimal(numero): 
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

        def octal(numero):
            octal = []
            
            while numero >= 1:
                octando = numero % 8
                numero = int(numero / 8) 
                octal.append(octando)

            octal.reverse()
            print(octal)
        
        def binário(numero):
            binario = []
            
            while numero >= 1:
                binariando = numero % 2
                numero = int(numero / 2) 
                binario.append(binariando)

            binario.reverse()
            print(binario)

        binário(numero)
        hexadecimal(numero)
        octal(numero)

    #Operação 2: Transformando numeros hexadecimais
    if operação == 2:
        def decimal(numero): 
            decimal = []
            numeroList = numero.split(",")
            quantidadesDeNumeros = len(numeroList) - 1

            while quantidadesDeNumeros >= 0:
                caractereParaConverter = numeroList.pop(quantidadesDeNumeros)

                try:
                    if isinstance(caractereParaConverter, str):
                        caractereParaConverter = int(caractereParaConverter)
                except ValueError:
                    pass

                
                if isinstance(caractereParaConverter, int):
                    if caractereParaConverter >= 0 and caractereParaConverter <= 9:
                        caractereConvertido = (16 ** quantidadesDeNumeros) * caractereParaConverter
                        print(caractereParaConverter)
                        print(caractereConvertido)
                        decimal.append(caractereConvertido)
                        quantidadesDeNumeros = quantidadesDeNumeros - 1
                if isinstance(caractereParaConverter, str):
                    if caractereParaConverter == "A":
                        caractereConvertido = (16 ** quantidadesDeNumeros) * 10
                        decimal.append(caractereConvertido)
                        quantidadesDeNumeros = quantidadesDeNumeros - 1

                    if caractereParaConverter == "B":
                        caractereConvertido = (16 ** quantidadesDeNumeros) * 11
                        decimal.append(caractereConvertido)
                        quantidadesDeNumeros = quantidadesDeNumeros - 1

                    if caractereParaConverter == "C":
                        decimal.remove("C")
                        caractereConvertido = (16 ** quantidadesDeNumeros + 1) * 12
                        decimal.append(caractereConvertido)
                        quantidadesDeNumeros = quantidadesDeNumeros - 1

                    if caractereParaConverter == "D":
                        caractereConvertido = (16 ** quantidadesDeNumeros + 1) * 13
                        decimal.remove("D")
                        decimal.append(caractereConvertido)
                        quantidadesDeNumeros = quantidadesDeNumeros - 1

                    if caractereParaConverter == "E":
                        caractereConvertido = (16 ** quantidadesDeNumeros + 1) * 14
                        decimal.remove(caractereParaConverter)
                        decimal.append(caractereConvertido)
                        quantidadesDeNumeros = quantidadesDeNumeros - 1

                    if caractereParaConverter == "F":
                        caractereConvertido = (16 ** quantidadesDeNumeros + 1) * 15
                        decimal.remove("F")
                        decimal.append(caractereConvertido)
                        quantidadesDeNumeros = quantidadesDeNumeros - 1

                #try:
                    #while True:
                            #decimal.remove("")
                #except ValueError:
                    #pass

            decimal.reverse()
            print(decimal)

        decimal(numero)

        



    
    
        
            
    




Programador()
    