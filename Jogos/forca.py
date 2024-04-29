import random


def mensagem_de_abertura():
    print("**************************************")
    print("---->xX Bem vindo ao jogo de Forca Xx<----")
    print("**************************************")

def carrega_palavra_secreta():
    
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    
    numero = random.randrange(0,len(palavras))
    
    palavra_secreta = palavras[numero].upper()
    
   
    
    return palavra_secreta

def carrega_espacos_de_palavras(palavra):
    return ["_" for letra in palavra]

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print(" /                   \ ")
    print(" |   XXXX     XXXX   |   ")
    print(" |   XXXX     XXXX   |     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def jogar():
    #começo do jogo
    
    mensagem_de_abertura()
   
    palavra_secreta = carrega_palavra_secreta()
    
    letras_acertadas = carrega_espacos_de_palavras(palavra_secreta)
    
    enforcou = False   
    acertou = False
    erros = 0
    
    
   
    print(letras_acertadas)
    #enquanto não ganhou ou perdeu
    while(not enforcou and not acertou):
        chute = input("Digite uma LETRAAAA: ")
        #retira os espaços e deixa tudo em maiusculo da variável chute
        chute = chute.strip().upper()
         
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    
                    letras_acertadas[index] = letra
                    
                    
                index += 1

        
        
        else:
            erros += 1
            desenha_forca(erros)
        #se erros for = 6, enforcou vira true
        enforcou = erros == 7
        #acertou vira true quando não há "_" nas letras_acertadas
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    
    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    
    
    
if(__name__ == "__main__"):
    jogar()