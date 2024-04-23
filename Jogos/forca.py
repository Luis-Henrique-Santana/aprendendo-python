def jogar():
    #começo do jogo
    print("**************************************")
    print("---->xX Bem vindo ao jogo de Forca Xx<----")
    print("**************************************")

    #.upper deixa tudo em maiusculo
    palavra_secreta = "batata".upper()
    
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    
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