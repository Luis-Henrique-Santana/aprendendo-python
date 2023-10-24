import random #importa a biblioteca de numeros aleatórios 

numrand = []  #cria o array numrand

for _ in range(10):  #inicia o laço de repetição
    rand = random.randint(1, 100) # pega um numero aleatório entre 1 e 100 e coloca na variavel rand
    numrand.append(rand) # coloca a variavel rand no final do vetor numrand (metodo append)

for numrand in numrand: #Cria um laço de repetição para imprimir a variavel numrand, assim fazendo pular linha
    print(numrand) #exibe os numeros aleatórios no vetor de forma a pular as linhas (caso seja na mesma linha só colocar o print)
