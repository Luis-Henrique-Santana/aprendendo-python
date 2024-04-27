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
        #se erros for = 6, enforcou vira true
        enforcou = erros == 6
        #acertou vira true quando não há "_" nas letras_acertadas
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    
    if(acertou):
        print("Parabens!!!\n Você venceu!!!")
    else:
        print("__\n | \n | \n 0 \n/|\ \n/ \ \n\n Perdeste ;-;\n")
    
    
    
if(__name__ == "__main__"):
    jogar()