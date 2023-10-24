class Geladeira:  # define uma classe chamada geladeira
    
    def __init__(self, marca, cor, anoDeFabricacao): #
        self.marca = marca
        self.cor = cor
        self.anoDeFabricacao = anoDeFabricacao
        self.estado = 'desligada' #atributo padrão para estado
        
    def ligar(self):
        self.estado = 'ligado'
    
    def desligar(self):
        self.estado = 'desligado'
        
        #Método para obtrer informações
    def obter_informacoes(self):
        return f"Carro: {self.marca} {self.cor} {self.anoDeFabricacao}"


minha_geladeira = Geladeira("Eletrolux", "hb20211", 2022)

minha_geladeira.ligar()
print(minha_geladeira.obter_informacoes())

minha_geladeira.desligar()
print(minha_geladeira.obter_informacoes())