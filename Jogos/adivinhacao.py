def jogar():
    import random

    print("**************************************")
    print("---->xX Bem vindo ao jogo de Adivinhação Xx<----")
    print("**************************************")


    numero_secreto = random.randint(1,100)

    vidas = 0
    pontos = 0
    erros = 0

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        vidas = 20
    elif (nivel == 2):
        vidas = 10
    else:
        vidas = 5



    while (vidas > 0):
        print("Vidas restantes: {}".format(vidas))
        tentativa = input("Digite o numero que você acha que é o correto ( entre 1 e 100 ): ")
        tentativa = int(tentativa)
        
        if(tentativa > 100 or tentativa < 1):
            print("É PARA DIGITAR UM NUMERO ENTRE  1  E  100")
            continue
        

        print("Você digitou ", tentativa)

        acertou = tentativa == numero_secreto
        menor = tentativa < numero_secreto
        maior = tentativa > numero_secreto

        if(acertou):
            print ("ACERTOU!!!!")
            break; 

        else:
            print("Errou!!!!")
            
            if(maior):
                print("Sua tentativa foi maior que o numero secreto")
            else:
                print("Sua tentativa foi menor que o numero secreto") 

            vidas = vidas - 1  
            erros +=1  
            
    pontos = (nivel * 1000)/erros

    print("Vidas restantes: ", vidas)
    print("pontuação: ", round(pontos))    
    print("...FIM...")

#verifica se o arquivo é o arquivo raiz

if(__name__ == "__main__"):
    jogar()