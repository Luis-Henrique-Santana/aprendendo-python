import random

print("**************************************")
print("---->xX Bem vindo ao jogo de Adivinhação Xx<----")
print("**************************************")

numero_secreto = random.randint(1,99)

print("DICA:", numero_secreto+1)

tentativa = input("Digite o numero que você acha que é o correto:")


tentativa = int(tentativa)

print("Você digitou ", tentativa)

if(tentativa == numero_secreto):
    print ("ACERTOU!!!!")

else:
    print("Errou!!!!")
    
print("...FIM...")
