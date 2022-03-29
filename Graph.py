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
        graph['Ra'] = [i for i in range(self.getSize()) ]#indices de la premiere rangée
        graph['Rb'] = [self.getSize() * (self.getSize() - 1) + i  for i in range(self.getSize()) ]#indices de la dernier rangée
        return graph

    def initGraphB(self):
        graph = {}
        graph['Ba'] = [i + self.getSize() for i in range(self.getSize()) ]
        graph['Bb'] = [(self.getSize() - 1) + i * self.getSize() for i in range(self.getSize()) ]
        return graph
        

    
    
    def ajoutSommet(self, indice, x): # indice Bleu ou Rouge 
        if (indice == 'R'):
            self.__graphR[x] = []
        

            i = int(x / self.__size)
            j = x % self.__size

            int v = (i-1)*self.__size+j

            if i-1 > 0 && v in self.__graphR.keys():
                self.__graphR[x].append(v)
                self.__graphR[v].append(x)

            v = (i+1)*self.__size+j

            if i+1 < self.__size && v in self.__graphR.keys():
                self.__graphR[x].append(v)
                self.__graphR[v].append(x)

            v = i*self.__size+j-1

            if j-1 > 0 && v in self.__graphR.keys():
                self.__graphR[x].append(v)
                self.__graphR[v].append(x)

            v = i*self.__size+j+1

            if j+1 < self.__size && v in self.__graphR.keys():
                self.__graphR[x].append(v)
                self.__graphR[v].append(x)

            v = (i-1)*self.__size+j+1

            if j+1 < self.__size && i-1 > 0 && v in self.__graphR.keys():
                self.__graphR[x].append(v)
                self.__graphR[v].append(x)

            v = (i+1)*self.__size+j-1

            if i+1 < self.__size && j-1 > 0 && v in self.__graphR.keys():
                self.__graphR[x].append(v)
                self.__graphR[v].append(x)


        elif(indice == 'B'):
            
            self.__graphB[x] = []
        

            i = int(x / self.__size)
            j = x % self.__size

            int v = (i-1)*self.__size+j

            if i-1 > 0 && v in self.__graphB.keys():
                self.__graphB[x].append(v)
                self.__graphB[v].append(x)

            v = (i+1)*self.__size+j

            if i+1 < self.__size && v in self.__graphB.keys():
                self.__graphB[x].append(v)
                self.__graphB[v].append(x)

            v = i*self.__size+j-1

            if j-1 > 0 && v in self.__graphB.keys():
                self.__graphB[x].append(v)
                self.__graphB[v].append(x)

            v = i*self.__size+j+1

            if j+1 < self.__size && v in self.__graphB.keys():
                self.__graphB[x].append(v)
                self.__graphB[v].append(x)

            v = (i-1)*self.__size+j+1

            if j+1 < self.__size && i-1 > 0 && v in self.__graphB.keys():
                self.__graphB[x].append(v)
                self.__graphB[v].append(x)

            v = (i+1)*self.__size+j-1

            if i+1 < self.__size && j-1 > 0 && v in self.__graphB.keys():
                self.__graphB[x].append(v)
                self.__graphB[v].append(x)
        else:
            print("wrong usage of indice: Blue or Rouge")

             
    


