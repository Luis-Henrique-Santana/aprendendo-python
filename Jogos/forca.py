def jogar():
    print("**************************************")
    print("---->xX Bem vindo ao jogo de Forca Xx<----")
    print("**************************************")

    palavra_secreta = "batata"
    enforcou = False   
    acertou = False
   
   #enquanto não ganhou ou perdeu
    while(not enforcou and not acertou):
        chute = input("Desce a LETRAAAA: ")
        chute = chute.strip()
        
        
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("encontrou a letra {} na posição {}".format(letra, index))
                index = index + 1

print("...FIM...")
    
    
    
    
    
if(__name__ == "__main__"):
    jogar()