class Geladeira:  # define uma classe chamada geladeira
    
    def __init__(self, marca, cor, anoDeFabricacao): #
        self.marca = marca
        self.cor = cor
        self.anoDeFabricacao = anoDeFabricacao
        self.estado = 'desligada' #atributo padrão para estado
        
    def ligar(self):# metodo para modificar o estado para ligado
        self.estado = 'ligada'
    
    def desligar(self): #metodo para modificar o estado para desligado
        self.estado = 'desligada'
        
        #Método para obtrer informações
    def obter_informacoes(self): #metodo para retornar as informações do objeto
        return f"Geladeira: {self.marca} {self.cor} {self.anoDeFabricacao} {self.estado}"


minha_geladeira = Geladeira("Eletrolux", "hb20211", 2022)

minha_geladeira.ligar()
print(minha_geladeira.obter_informacoes())

minha_geladeira.desligar()
print(minha_geladeira.obter_informacoes())