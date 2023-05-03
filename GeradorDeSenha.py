import random

def geraSenha():
    print("Gerador de senhas")
    caracteres = "`1234567890-=!@#$%^&*()_+qwertyuiop[]\sadfghjkl;'zxcvbnm,./QWERTYUIOP{|}ASDFGHJKL:ZXCVBNM<>?~"
    qtd_senhas = int(input("Quantas senhas você quer gerar?"))
    qtd_caracteres = int(input("Quantos caracteres você quer que sua senha tenha?"))

    def senha(qtd_caracteres):
        senhaGerada = ""
        while qtd_caracteres > 0:
            senhaGerada += random.choice(caracteres)
            qtd_caracteres -= 1
        print(senhaGerada)
                

    def fazSenha(qtd_senhas):
        print("\nSuas senhas geradas:")
        while qtd_senhas > 0:
            qtd_senhas -= 1
            senha(qtd_caracteres)
            

            

    fazSenha(qtd_senhas)
geraSenha()
            
