def jogar():
    #começo do jogo
    print("**************************************")
    print("---->xX Bem vindo ao jogo de Forca Xx<----")
    print("**************************************")

    palavra_secreta = "batata"
    
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    
    enforcou = False   
    acertou = False
   
    print(letras_acertadas)
    #enquanto não ganhou ou perdeu
    while(not enforcou and not acertou):
        chute = input("Desce a LETRAAAA: ")
        chute = chute.strip()
         
        
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                
                letras_acertadas[index] = letra
                
                
            index = index + 1

        print(letras_acertadas)
    
    
    
    
    
if(__name__ == "__main__"):
    jogar()