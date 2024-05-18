import matplotlib.pyplot as plt
from random import random

class Produto():
    def __init__(self, nome, espaço, valor):
        self.nome = nome
        self.espaco = espaço
        self.valor = valor
        
class Individuo():
    def __init__(self, espacos, valores, limites_espacos, geracao = 0):
        self.espacos = espacos
        self.valores = valores
        self.limites_espacos = limites_espacos
        self.geracao = geracao
        self.nota_avaliacao = 0
        self.espaco_usado = 0
        self.cromossomo = []
        
        for i in range(len(espacos)):
            if random() < 0.5:
                self.cromossomo.append(0)
            else:
                self.cromossomo.append(1)

    def avaliacao(self):
        nota = 0
        soma_espacos = 0
        for i in range(len(self.cromossomo)):
            if self.cromossomo[i] == '1':
                nota += self.valores[i]
                soma_espacos += self.espacos[i]
                
        if soma_espacos > self.limites_espacos:
            nota = 1
            
        self.nota_avaliacao = nota
        self.espaco_usado = soma_espacos
        
    def mutacao(self, taxa_mutacao):
        
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if self.cromossomo[i] == '1':
                    self.cromossomo[i] = '0'
                else:
                    self.cromossomo[i] = '1'
        return self
    
    def crossover(self, outro_individuo):
        corte = round(random()) * len((self.cromossomo))
        
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]
        
        filhos = [individuo(self.espacos, self.valores, self.limites_espacos, self.geracao + 1),
               individuo(self.espacos, self.valores, self.limites_espacos, self.geracao + 1)]
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        
        return filhos
    
class AlgoritmoGenetico():
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = [] #populacao atual do ciclo
        self.geracao = 0
        self.melhor_solucao = 0
        self.lista_solucoes = []
        
    def inicia_populacao(self):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(espacos, valores, limites_espacos))
        self.melhor_solucao = self.populacao(0)
    
    def ordena_populacao(self):
        self.populacao = sorted(self.populacao, 
                                key = lambda populacao.nota_avaliacao, reverse = True)
                              
    def melhor_individuo(self, melhor_individuo_atual):
        if melhor_individuo_atual.nota_avaliacao > self.melhor_solucao.nota_avaliacao
            self.melhor_solucao = melhor_individuo_atual
        
    def soma_avaliacao(self):
        soma = 0
        for individuo in self.populacao:
            soma += individuo.nota_avaliacao
            
        return soma
        
    def visualiza_geracao(self):
        melhor = self.populacao(0)
        print("G: %s -> valor: %s Espaço: %s cromossomo: %s" %( 
            self.populacao[0].geracao, 
            melhor.nota_avaliacao, 
            melhor.espaco_usado, 
            melhor.cromossomo))
        
    def seleciona_pai(self, soma_avaliacao):
        valor_sorteado = random() * soma_avaliacao
        i = 0
        soma = 0
        pai = -1 
        while i < len(self.populacao) and soma < valor_sorteado:
            soma += self.populacao[i].nota_avaliacao
            pai += 1
            i += 1 
        return pai
    
    
    def resolver(self, taxa_mutacao, numero_geracoes, espacos,
                 valores, limites_espacos):
        
        inicia_populacao(espacos, valores, limites_espacos)
        
        for individuo in self.populacao:
            individuo.avaliacao()
            
        ordena_populacao()
        self.melhor_solucao = self.populacao[0]
        self.lista_solucoes.append(self.populacao[0].nota_avaliacao)
        visualiza_geracao()
        
        for geracao in range(numero_geracoes):
            soma_avaliacao = soma_avaliacoes()
            nova_populacao = []
            
            for individuos_gerados in range(0, self.tamanho_populacao, 2):
                pai1 = seleciona_pai(self, soma_avaliacao)
                pai2 = seleciona_pai(self, soma_avaliacao)
                
                filhos = self.populacao[pai1].crossover(self.populacao[pai2])
                
                nova_populacao.append(filhos[0].mutacao(taxa_mutacao))
                nova_populacao.append(filhos[1].mutacao(taxa_mutacao))
        self.populacao = list(nova_populacao)
        
        for individuo in self.populacao:
            individuo.avaliacao()
            
        ordena_populacao()
        visualiza_geracao()
        
        melhor_geracao = self.populacao[0]
        self.lista_solucoes.append(melhor_geracao.nota_avaliacao)
        melhor_individuo(melhor_geracao)
    
        print("melhor Solução: G: %s Valor: %s Espaço: %s Cromossomo %s" %(
            self.melhor_solucao.geracao,
            self.melhor_solucao.nota_avaliacao,
            self.melhor_solucao.espaco_usado,
            self.melhor_solucao.cromossomo))
        return self.melhor_geracao.cromossomo 
    
    
        
        
lista_produtos = []
lista_produtos.append(produto("Geladeira", 0.751, 999.99))
lista_produtos.append(produto("Iphone", 0.000089, 2911.12))
lista_produtos.append(produto("TV 55", 0.400, 4346.99))
lista_produtos.append(produto("TV 50", 0.290, 3999.99))
lista_produtos.append(produto("TV 42", 0.200, 2999.99))
lista_produtos.append(produto("Notebook dell", 0.00350, 2499.90))
lista_produtos.append(produto("Ventilador", 0.0496, 199.99))
lista_produtos.append(produto("Microondas Electo", 0.0424, 308.66))
lista_produtos.append(produto("Microondas LG", 0.544, 429.90))
lista_produtos.append(produto("Notebook lenovo", 0.00450, 1999.99))
lista_produtos.append(produto("Notebook Asus", 0.00390, 1999.89))
lista_produtos.append(produto("Fogao 4b", 0.450, 1200.55))
lista_produtos.append(produto("Fogao 4b", 0.541, 1890.99))

limite = 3 #limite de metragem cubica caminhao
tamanho_populacao = 20
taxa_mutacao = 0.01
numero_geracoes = 1000

espacos = []
valores = []
nomes = []

for produto in lista_produtos:
    espacos.append(produto.espaco)
    valores.append(produto.valor)
    nomes.append(produto.nome)
    
ag = AlgoritmoGenetico(tamanho_populacao)

resultado = ag.resolver(taxa_mutacao, numero_geracoes, espacos, valores, limites_espacos)
