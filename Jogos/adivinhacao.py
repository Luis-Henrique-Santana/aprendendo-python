import random

print("**************************************")
print("---->xX Bem vindo ao jogo de Adivinhação Xx<----")
print("**************************************")

numero_secreto = random.randint(1,99)

tentativa = input("Digite o numero que você acha que é o correto:")

tentativa = int(tentativa)

print("Você digitou ", tentativa)

acertou = tentativa == numero_secreto
menor = tentativa < numero_secreto
maior = tentativa > numero_secreto

if(acertou):
    print ("ACERTOU!!!!")

else:
    print("Errou!!!!")
    
    if(maior):
        print("Sua tentativa foi maior que o numero secreto")
    else:
        print("Sua tentativa foi menor que o numero secreto")    
    
    
print("...FIM...")
