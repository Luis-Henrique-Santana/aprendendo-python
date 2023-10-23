#codigo de fib

#n1 = 0   #cria variavel 1
#n2 = 1 # cria variavel 2
#aux = 0  #Cria variavel auxiliar
#cont = 0  #Cria variavel contador

n1, n2, aux, cont = 0, 1, 0, 0 #cria todas em sequência

while cont<50:  #inicia o laço de repetição da sequencia
    print(n2,' ')  # imprime o valor da variavel 2
    aux = n1+n2  # soma a variavel 1 e 2 na auxiliar
    n1 = n2    # transforma a variavel 1 na 2
    n2 = aux  # coloca a auxiliar na variavel 2
    cont = cont+1 # adiciona 1 no contador

