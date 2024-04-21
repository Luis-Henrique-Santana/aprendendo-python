import math
import matplotlib.pyplot as plt

class vetorPadrao:
    def __init__(self, X, Y, Anterior, Distancia): 
        self.X = X
        self.Y = Y
        self.Anterior = Anterior
        self.Distancia = Distancia
 
class buscarLabirinto:
    def __init__(self, corpo, inicio, fim, tamanho):
        self.corpo = corpo
        self.iniciox = inicio[0]
        self.inicioy = inicio[1]
        self.fimx = fim[0]
        self.fimy = fim[1]
        self.tamanhox = tamanho[0]
        self.tamanhoy = tamanho[1]
        self.vetorAberto = []
        self.vetorFechado = []
        self.vetorCaminhoFinal = []
    
    
    def verNovosVizinhos(self, x, y):
        saida = []
        #x+1 y-1
        if((y-1>=0 ) and (x+1 <= self.tamanhox)):
            if(self.corpo[x+1][y-1] == 1):
                if(self.verificarExistenciaVetorFechado(x+1, y-1) == False):
                    if(self.verificarExistenciaVetorAberto(x+1, y-1) == False):
                        saida.append([x+1,y-1])
              
         #x+1,y
        if ((x+1 <= self.tamanhox)):
            if(self.corpo[x+1][y] == 1):
                if (self.verificarExistenciaVetorAberto(x+1, y) == False):
                    if(self.verificarExistenciaVetorFechado(x+1, y) == False):
                        saida.append([x+1,y])
                        
        #x+1 y+1
        if((y+1<=self.tamanhoy ) and (x+1 <= self.tamanhox)):
            if(self.corpo[x+1][y+1] == 1):
                if(self.verificarExistenciaVetorFechado(x+1, y+1) == False):
                    if(self.verificarExistenciaVetorAberto(x+1, y+1) == False):
                        saida.append([x+1,y+1])
        
        #x y+1
        if(y+1<=self.tamanhoy ):
            if(self.corpo[x][y+1] == 1):
                if(self.verificarExistenciaVetorFechado(x, y+1) == False):
                    if(self.verificarExistenciaVetorAberto(x, y+1) == False):
                        saida.append([x,y+1])
        
        #x y-1
        if(y-1<=0 ):
            if(self.corpo[x][y-1] == 1):
                if(self.verificarExistenciaVetorFechado(x, y-1) == False):
                    if(self.verificarExistenciaVetorAberto(x, y-1) == False):
                        saida.append([x,y-1])
                        
        #x-1 y-1
        if((x-1 >= 0) and (y-1<=0) ):
            if(self.corpo[x-1][y-1] == 1):
                if(self.verificarExistenciaVetorFechado(x-1, y-1) == False):
                    if(self.verificarExistenciaVetorAberto(x-1, y-1) == False):
                        saida.append([x-1,y-1])
        
        #x-1 y
        if(x-1 >= 0):
            if(self.corpo[x-1][y] == 1):
                if(self.verificarExistenciaVetorFechado(x-1, y) == False):
                    if(self.verificarExistenciaVetorAberto(x-1, y) == False):
                        saida.append([x-1,y])
        
        #x-1 y+1
        if((x-1 >= 0) and (y+1<=self.tamanhoy) ):
            if(self.corpo[x-1][y+1] == 1):
                if(self.verificarExistenciaVetorFechado(x-1, y+1) == False):
                    if(self.verificarExistenciaVetorAberto(x-1, y+1) == False):
                        saida.append([x-1,y+1])
                        
        return saida;
    
    def verificarExistenciaVetorAberto(self,x,y):
        #Roda o vetor aberto conferindo se o x,y esta la
        for i in self.vetorAberto:
            if((i.X == x) and (i.Y == y)):
                return True
        return False
    
    def verificarExistenciaVetorFechado(self,x,y): 
        for i in self.vetorFechado:
            if(i.X == x) and (i.Y == y):
                return True
        return False
    
    def verificarDistanciaXY(self, x, y, x0, y0):
        
    
        dist = math.sqrt(
            math.fabs(math.pow(x-x0,2)) +
            math.fabs(math.pow(y-y0,2))
            ) 
        
        return round(dist,3);
    
    def avaliarVizinhosEVetorAberto(self, vizinhos, posicaoVetorFechado):
        semVizinho = False
        posControle = 0
        controle = 999999
        vetorControle = []
    #verificar se vizinhos e vetorAberto estão vazios, para casos sem solução
        if((len(vizinhos) == 0) and (len(self.vetorAberto) == 0)):
            print("sem solução!!")
            return False
        
        
        #Roda os novos vizinhos validando a distancia e pegando o melhor vizinho
        c=0
        for i in vizinhos:
            tempDistancia = self.verificarDistanciaXY(i[0], i[1], self.fimx, self.fimy)
            vetorControle.append(vetorPadrao(i[0], i[1], posicaoVetorFechado, tempDistancia))
            if(c==0):
                controle = tempDistancia
            else:
                if(tempDistancia<controle):
                    controle = tempDistancia
                    posControle = c
            c = c + 1
        
        #roda o vetorAberto pegando o melhor resultado
        c = 0 
        for i in self.vetorAberto:
            if(i.Distancia < controle):
                controle = i.Distancia
                posControle = c
                semVizinho = True
            c = c + 1 
        
        #Verifica se a melhor resposta é vetorAberto 
        #ou um vizinho novo e distribui as variáveis
        addVetorFechado = []
        if(semVizinho == True):
            addVetorFechado.append(self.vetorAberto[posControle])
            del self.vetorAberto[posControle]
        else:
            addVetorFechado.append(vetorControle[posControle])
            del vetorControle[posControle]
        self.vetorFechado.append(addVetorFechado[0])
        
        for i in vetorControle:
            self.vetorAberto.append(i)
        return True
 
    def gerarCaminhoFinal(self):
        self.vetorCaminhoFinal.clear()
        controle = -1
        while (controle != 0):
            if(controle == -1):
                self.vetorCaminhoFinal.append(self.vetorFechado[len(self.vetorFechado) - 1])
                controle = self.vetorFechado[len(self.vetorFechado) - 1].Anterior
            else:
                self.vetorCaminhoFinal.append(self.vetorFechado[controle])
                controle = self.vetorFechado[controle].Anterior
            
            self.vetorCaminhoFinal.append(self.vetorFechado[0])

    def gerarGrafico(self):
        plt.xlim(0, self.tamanhoy + 2)
        plt.ylim(0, self.tamanhox + 2)
        corpo = self.corpo
        
        for i in self.vetorCaminhoFinal:
            corpo[i.X][i.Y] = "X"
        
        c=1
        corpo.reverse()
        for i in corpo:
            d=1
            for j in i:
                if(j == 1):
                    cor = 'blue'
                elif(j == 0):
                    cor = 'grey'
                elif(j == "X"):
                    cor = 'green'    
                plt.text(d,c,j,backgroundcolor = cor)  
                d = d + 1
            c = c + 1    
        plt.show()
        
    def buscarCaminho(self):
        self.vetorFechado.append(vetorPadrao(self.iniciox, 
                                             self.inicioy, 
                                             0, 
                                             self.verificarDistanciaXY
                                             (self.iniciox, 
                                              self.inicioy, 
                                              self.fimx, 
                                              self.fimy
                                              )
                                             )
                                 )
        saida = 0 
        while (saida == 0):
            if(self.vetorFechado == 0):
                saida = 1
            else:
                x = self.vetorFechado[-1].X
                y = self.vetorFechado[-1].Y
                posicaoVetorFechado = len(self.vetorFechado) - 1
                vizinhos = self.verNovosVizinhos(x, y)
                
                status = self.avaliarVizinhosEVetorAberto(vizinhos, posicaoVetorFechado)
                if((self.vetorFechado[-1].Distancia > 0) and (status == True)):
                    saida = 0 
                else:
                    saida = 1
            
        self.gerarCaminhoFinal()
        self.gerarGrafico()
        
                
                
#---- CORPO PRINCIPAL -------

corpo = [[1,1,0,0,0,0,1,1],
         [1,0,0,1,1,0,0,1],
         [1,1,0,1,1,1,0,1],
         [1,1,1,1,0,1,1,1]]

tamanho = [3,7]

inicio = [0,0]

final = [0,7]

chamada = buscarLabirinto(corpo, inicio, final, tamanho)

#----------------- AREA DE TESTES --------------

chamada.buscarCaminho()



#Professor Bruno Baruffi Esteves
#Segunda parte do algoritmo de busca A*
