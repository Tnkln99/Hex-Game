class Graph:
    
    def __init__(self,size):
        self.__graphR = self.initGraphR()
        self.__graphB = self.initGraphB()
        self.__size = size
    
    #getters 
    def getSize(self):
        return self.__size

    def getGraphR(self):
        return self.__graphR

    def getGraphB(self):
        return self.__graphB
 
    def initGraphR(self):
        graph = {}
        graph['Ra'] = [i for i in range(self.getSize()) ]
        graph['Rb'] = [self.getSize() * (self.getSize() - 1) + i  for i in range(self.getSize()) ]
        return graph

    def initGraphB(self):
        graph = {}
        graph['Ba'] = [i + self.getSize() for i in range(self.getSize()) ]
        graph['Bb'] = [(self.getSize() - 1) + i * self.getSize() for i in range(self.getSize() - 1) ]
        return graph
        

    
    
    def ajoutSommet(self, indice, x): # indice Bleu ou Rouge 
        if (indice == 'R'):
            self.__graphB.ajout(x)
            for i in self.__graphB:
                 for k in i.value():
                     if k == x:
                         x.value.append(k)
                         self.__graphB[k].append(x)
        elif(indice == 'B'):
            self.__graphB.ajout(x)
            for i in self.__graphB:
                 for k in i.value():
                     if k == x:
                         x.value.append(k)
                         self.__graphB[k].append(x)
        else:
            print("wrong usage of indice: Blue or Rouge")

             
    


