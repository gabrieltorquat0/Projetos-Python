x0 = 0
x1 = 1
x2 = 2
x3 = 3
x4 = 4
x5 = 5
x6 = 6
x7 = 7
x8 = 8

print("| ", x0, " | ", x1, " | ", x2, " | ")
print("| ", x3, " | ", x4, " | ", x5, " | ")
print("| ", x6, " | ", x7, " | ", x8, " | ")

def jogoDaVelha(turno, x0, x1, x2, x3, x4, x5, x6, x7, x8):
    if x0 == "X" and x1 == "X" and x2 == "X" or x3 == "X" and x4 == "X" and x5 == "X" or x6 == "X" and x7 == "X" and x8 == "X":
        print("X GANHOU!")
        turno = ""
    elif x0 == "○" and x1 == "○" and x2 == "○" or x3 == "○" and x4 == "○" and x5 == "○" or x6 == "○" and x7 == "○" and x8 == "○":
        print("○ GANHOU")
        turno = ""
    elif x0 == "X" and x3 == "X" and x6 == "X" or x1 == "X" and x4 == "X" and x7 == "X" or x2 == "X" and x5 == "X" and x8 == "X":
        print("X GANHOU")
        turno = ""
    elif x0 == "○" and x3 == "○" and x6 == "○" or x1 == "○" and x4 == "○" and x7 == "○" or x2 == "○" and x5 == "○" and x8 == "○":
        print("○ GANHOU")
        turno = ""
    elif x0 == "X" and x4 == "X" and x8 == "X" or x2 == "X" and x4 == "X" and x6 == "○": 
        print("X GANHOU")
        turno = ""
    elif x0 == "○" and x4 == "○" and x8 == "○" or x2 == "○" and x4 == "○" and x6 == "○": 
        print("○ GANHOU")
        turno = ""

    while turno == False:
        jogada = input("TURNO X, faça sua jogada (0-8):")
        jogada = int(jogada)
        if jogada == 0: 
            x0 = "X"
            #turno == True
            print("| ", x0, " | ", x1, " | ", x2, " | ")
            print("| ", x3, " | ", x4, " | ", x5, " | ")
            print("| ", x6, " | ", x7, " | ", x8, " | ")
            return jogoDaVelha(True, x0, x1, x2, x3, x4, x5, x6, x7, x8)
        elif jogada == 1: 
            x1 = "X"
            turno = True
            print("| ", x0, " | ", x1, " | ", x2, " | ")
            print("| ", x3, " | ", x4, " | ", x5, " | ")
            print("| ", x6, " | ", x7, " | ", x8, " | ")
            return jogoDaVelha(True, x0, x1, x2, x3, x4, x5, x6, x7, x8)
        if jogada == 2: 
            x2 = "X"
            turno = True
            print("| ", x0, " | ", x1, " | ", x2, " | ")
            print("| ", x3, " | ", x4, " | ", x5, " | ")
            print("| ", x6, " | ", x7, " | ", x8, " | ")
            return jogoDaVelha(True, x0, x1,x2, x3, x4, x5, x6, x7, x8)
        if jogada == 3: 
            x3 = "X"
            turno = True
            print("| ", x0, " | ", x1, " | ", x2, " | ")
            print("| ", x3, " | ", x4, " | ", x5, " | ")
            print("| ", x6, " | ", x7, " | ", x8, " | ")
            return jogoDaVelha(True, x0, x1, x2, x3, x4, x5, x6, x7, x8)
        if jogada == 4: 
            x4 = "X"
            turno = True
            print("| ", x0, " | ", x1, " | ", x2, " | ")
            print("| ", x3, " | ", x4, " | ", x5, " | ")
            print("| ", x6, " | ", x7, " | ", x8, " | ")
            return jogoDaVelha(True, x0, x1, x2, x3, x4, x5, x6, x7, x8)
        if jogada == 5: 
            x5 = "X"
            turno = True
            print("| ", x0, " | ", x1, " | ", x2, " | ")
            print("| ", x3, " | ", x4, " | ", x5, " | ")
            print("| ", x6, " | ", x7, " | ", x8, " | ")
            return jogoDaVelha(True, x0, x1, x2, x3, x4, x5, x6, x7, x8)
        if jogada == 6: 
            x6 = "X"
            turno = True
            print("| ", x0, " | ", x1, " | ", x2, " | ")
            print("| ", x3, " | ", x4, " | ", x5, " | ")
            print("| ", x6, " | ", x7, " | ", x8, " | ")
            return jogoDaVelha(True, x0, x1, x2, x3, x4, x5, x6, x7, x8)
        if jogada == 7: 
            x7 = "X"
            turno = True
            print("| ", x0, " | ", x1, " | ", x2, " | ")
            print("| ", x3, " | ", x4, " | ", x5, " | ")
            print("| ", x6, " | ", x7, " | ", x8, " | ")
            return jogoDaVelha(True, x0, x1, x2, x3, x4, x5, x6, x7, x8)
        if jogada == 8: 
            x8 = "X"
            turno = True
            print("| ", x0, " | ", x1, " | ", x2, " | ")
            print("| ", x3, " | ", x4, " | ", x5, " | ")
            print("| ", x6, " | ", x7, " | ", x8, " | ")
            return jogoDaVelha(True, x0, x1, x2, x3, x4, x5, x6, x7, x8)


    while turno == True:
        jogada = int(input("Turno Y, insira sua jogada (0-8):"))
        if jogada == 0: 
            x0 = "○"
            turno == False
            print("| ", x0, " | ", x1, " | ", x2, " | ")
            print("| ", x3, " | ", x4, " | ", x5, " | ")
            print("| ", x6, " | ", x7, " | ", x8, " | ")
            return jogoDaVelha(False, x0, x1, x2, x3, x4, x5, x6, x7, x8)
        if jogada == 1: 
            x1 = "○"
            turno = False
            print("| ", x0, " | ", x1, " | ", x2, " | ")
            print("| ", x3, " | ", x4, " | ", x5, " | ")
            print("| ", x6, " | ", x7, " | ", x8, " | ")
            return jogoDaVelha(False, x0, x1, x2, x3, x4, x5, x6, x7, x8)
        if jogada == 2: 
            x2 = "○"
            turno = False
            print("| ", x0, " | ", x1, " | ", x2, " | ")
            print("| ", x3, " | ", x4, " | ", x5, " | ")
            print("| ", x6, " | ", x7, " | ", x8, " | ")
            return jogoDaVelha(False, x0, x1, x2, x3, x4, x5, x6, x7, x8)
        if jogada == 3: 
            x3 = "○"
            turno = False
            print("| ", x0, " | ", x1, " | ", x2, " | ")
            print("| ", x3, " | ", x4, " | ", x5, " | ")
            print("| ", x6, " | ", x7, " | ", x8, " | ")
            return jogoDaVelha(False, x0, x1, x2, x3, x4, x5, x6, x7, x8)
        if jogada == 4: 
            x4 = "○"
            turno = False
            print("| ", x0, " | ", x1, " | ", x2, " | ")
            print("| ", x3, " | ", x4, " | ", x5, " | ")
            print("| ", x6, " | ", x7, " | ", x8, " | ")
            return jogoDaVelha(False, x0, x1, x2, x3, x4, x5, x6, x7, x8)
        if jogada == 5: 
            x5 = "○"
            turno = False
            print("| ", x0, " | ", x1, " | ", x2, " | ")
            print("| ", x3, " | ", x4, " | ", x5, " | ")
            print("| ", x6, " | ", x7, " | ", x8, " | ")
            return jogoDaVelha(False, x0, x1, x2, x3, x4, x5, x6, x7, x8)
        if jogada == 6: 
            x6 = "○"
            turno = False
            print("| ", x0, " | ", x1, " | ", x2, " | ")
            print("| ", x3, " | ", x4, " | ", x5, " | ")
            print("| ", x6, " | ", x7, " | ", x8, " | ")
            return jogoDaVelha(False, x0, x1, x2, x3, x4, x5, x6, x7, x8)
        if jogada == 7: 
            x7 = "○"
            turno = False
            print("| ", x0, " | ", x1, " | ", x2, " | ")
            print("| ", x3, " | ", x4, " | ", x5, " | ")
            print("| ", x6, " | ", x7, " | ", x8, " | ")
            return jogoDaVelha(False, x0, x1, x2, x3, x4, x5, x6, x7, x8)
        if jogada == 8: 
            x8 = "○"
            turno = False
            print("| ", x0, " | ", x1, " | ", x2, " | ")
            print("| ", x3, " | ", x4, " | ", x5, " | ")
            print("| ", x6, " | ", x7, " | ", x8, " | ")
            return jogoDaVelha(False, x0, x1, x2, x3, x4, x5, x6, x7, x8)

jogoDaVelha(False, 0, 1, 2, 3, 4, 5, 6, 7, 8)
