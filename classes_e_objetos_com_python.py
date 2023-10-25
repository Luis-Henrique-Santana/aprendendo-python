import sys #importa a biblioteca sys

class Geladeira:  # define uma classe chamada geladeira
    
    def __init__(self, marca, cor, anoDeFabricacao): # inicia os atributos do objeto
        self.marca = marca #iguala atributo a uma variavel
        self.cor = cor #iguala atributo a uma variavel
        self.anoDeFabricacao = anoDeFabricacao #iguala atributo a uma variavel
        self.estado = 'desligada' #atributo padrão para estado
        
    def ligar(self):# metodo para modificar o estado para ligado
        self.estado = 'ligada'
    
    def desligar(self): #metodo para modificar o estado para desligado
        self.estado = 'desligada'
        
        #Método para obtrer informações
    def obter_informacoes(self): #metodo para retornar as informações do objeto
        return f"Geladeira: {self.marca} {self.cor} {self.anoDeFabricacao} {self.estado}"#retorna as informações do objeto
    
#fim da classe geladeira

while True: #iniciando laço infinito para verificar se deseja voltar ao programa
    marca = input("digite a marca da geladeira: ")# entrada da marca pelo usuario
    
    cor = input("digite a cor da geladeira: ")# entrada da cor pelo usuario
    
    
    
    while True: #criação do laço para verificar se a entrada é int
        try:
            ano = int(input("digite o ano da geladeira: "))# entrada do ano pelo usuario
            break #encerra o laço após a verificação da entrada
        except ValueError:
            print("Isso não é um número inteiro válido. Tente novamente.")
      
      
    minha_geladeira = Geladeira(marca, cor, int(ano))  #cria um objeto da classe Geladeira
      
    while True: # cria um laço para verificar se a entrada é zero ou um
        while True: #cria um laço para verificar se a entrada é um numero
            try:   
                estado = int(input("digite 1 para ligado e 0 para desligado: "))# entrada do estado pelo usuario
                break #encerra o laço após a verificação da entrada
            except ValueError:
                print("Isso não é um número válido. Tente novamente.")



        if int(estado) == 1: #estrutura de decisão para verificar se a geladeira será ligada            
            minha_geladeira.ligar() #usa o metodo ligar da classe e exibe informações 
            break #encerra o laço
    
    
        
        elif int(estado) == 0: #estrutura de decisão para verificar se a geladeira será desligada
            minha_geladeira.desligar()#usa o metodo desligar da classe e exibe informações
            break #encerra o laço
      
      
        
        else: #criação de uma resposta caso o estado não seja adequado
            print("Estado inexistente, tente novamente ") 
    
    print(minha_geladeira.obter_informacoes())  #mostra o resultado do metodo obter_informacoes da minha geladeira
      
    resposta = input("Deseja reiniciar o programa?(s/n) ") #inserção para saber se o usuario irá utilizar o programa novamente
    if resposta.lower() !='s': #faz o caractere ficar minúsculo
         sys.exit() #encerra o programa caso haja resposta negativa

 

    
