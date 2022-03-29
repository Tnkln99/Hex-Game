class Graph:
    
    def __init__(self,size):
        self.__size = size
        self.__graphR = self.initGraphR() #LA GRAPHE DE CONNEXTION ROUGE
        self.__graphB = self.initGraphB()
    
    #getters 
    def getSize(self):
        return self.__size

    def getGraphR(self):
        return self.__graphR

    def getGraphB(self):
        return self.__graphB
 
    def initGraphR(self):
        graph = {}
        graph['Ra'] = [i for i in range(self.__size) ]#indices de la premiere rangée
        graph['Rb'] = [self.__size * (self.getSize() - 1) + i  for i in range(self.getSize()) ]#indices de la dernier rangée
        return graph

    def initGraphB(self):
        graph = {}
        graph['Ba'] = [i * self.getSize() for i in range(self.getSize()) ]
        graph['Bb'] = [(self.getSize() - 1) + i * self.getSize() for i in range(self.getSize()) ]
        return graph
        

    
    
    def ajoutSommet(self, couleur, x): # couleur Bleu ou Rouge 
        if (couleur == "#FF0000"): #rouge
            self.__graphR[x] = []
        
#converir l'indice k en deux coordonnes (x,y), pour verifier les depassements
            i = int(x / self.__size)
            j = x % self.__size


#pour chaque voisin possible, on verifie le depassment, si c bon on cherche si il appartient a liste des keys de grapheB / grapheR

            if x in self.__graphR['Ra']:
                self.__graphR[x].append('Ra')

            if x in self.__graphR['Rb']:
                self.__graphR[x].append('Rb')


            v = (i-1)*self.__size+j  #reconvertir en indice unidimensionnel
    
            if i-1 > 0 and v in self.__graphR.keys():#ajouter les voisins dans les deux sens
                self.__graphR[x].append(v)
                self.__graphR[v].append(x)

            v = (i+1)*self.__size+j

            if i+1 < self.__size and v in self.__graphR.keys():
                self.__graphR[x].append(v)
                self.__graphR[v].append(x)

            v = i*self.__size+j-1

            if j-1 > 0 and v in self.__graphR.keys():
                self.__graphR[x].append(v)
                self.__graphR[v].append(x)

            v = i*self.__size+j+1

            if j+1 < self.__size and v in self.__graphR.keys():
                self.__graphR[x].append(v)
                self.__graphR[v].append(x)

            v = (i-1)*self.__size+j+1

            if j+1 < self.__size and i-1 > 0 and v in self.__graphR.keys():
                self.__graphR[x].append(v)
                self.__graphR[v].append(x)

            v = (i+1)*self.__size+j-1

            if i+1 < self.__size and j-1 > 0 and v in self.__graphR.keys():
                self.__graphR[x].append(v)
                self.__graphR[v].append(x)




        elif(couleur == "#0000FF"): #bleu
            self.__graphB[x] = []

            if x in self.__graphB['Ba']:
                self.__graphB[x].append('Ba')

            if x in self.__graphB['Bb']:
                self.__graphB[x].append('Bb')
        

            i = int(x / self.__size)
            j = x % self.__size

            v = (i-1)*self.__size+j

            if i-1 > 0 and v in self.__graphB.keys():
                self.__graphB[x].append(v)
                self.__graphB[v].append(x)

            v = (i+1)*self.__size+j

            if i+1 < self.__size and v in self.__graphB.keys():
                self.__graphB[x].append(v)
                self.__graphB[v].append(x)

            v = i*self.__size+j-1

            if j-1 > 0 and v in self.__graphB.keys():
                self.__graphB[x].append(v)
                self.__graphB[v].append(x)

            v = i*self.__size+j+1

            if j+1 < self.__size and v in self.__graphB.keys():
                self.__graphB[x].append(v)
                self.__graphB[v].append(x)

            v = (i-1)*self.__size+j+1

            if j+1 < self.__size and i-1 > 0 and v in self.__graphB.keys():
                self.__graphB[x].append(v)
                self.__graphB[v].append(x)

            v = (i+1)*self.__size+j-1

            if i+1 < self.__size and j-1 > 0 and v in self.__graphB.keys():
                self.__graphB[x].append(v)
                self.__graphB[v].append(x)
        else:
            print("wrong usage of couleur: Blue or Rouge")



    def gagnantB(self):
        # Use BFS to check path between s and d
        # Mark all the vertices as not visited
        visited =[False]*(self.__size * self.__size + 2)

         # Create a queue for BFS
        queue=[]

            # Mark the source node as visited and enqueue it
        queue.append('Ba')
        visited['Ba'] = True

        while queue:
     
                #Dequeue a vertex from queue
            n = queue.pop(0)

                # If this adjacent node is the destination node,
                # then return true
            if n == 'Bb':
                return True
     
                #  Else, continue to do BFS
            for i in self.__graphB[n]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
             # If BFS is complete without visited d
        return False

    def gagnantR(self):
        # Use BFS to check path between s and d
        # Mark all the vertices as not visited
        visited =[False]*(self.__size * self.__size)

         # Create a queue for BFS
        queue=[]

            # Mark the source node as visited and enqueue it
        queue.append('Ra')
        visited['Ra'] = True

        while queue:
     
                #Dequeue a vertex from queue
            n = queue.pop(0)

                # If this adjacent node is the destination node,
                # then return true
            if n == 'Rb':
                return True
     
                #  Else, continue to do BFS
            for i in self.__graphR[n]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
             # If BFS is complete without visited d
        return False

             
    


