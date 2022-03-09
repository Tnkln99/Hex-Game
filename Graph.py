class Graph:
    
    def __init__(self,size):
        self.__gagnant = ""
        self.__graph = self.__initGraph(size)
        self.__sommets = []
        self.__size = size
    

    # initialise graph comme = {0:[], 1:[], 2:[], ....}
    def __initGraph(size):
        sommetes = [i for i in range(size * size)]
        voisin = [[] for i in range(size * size)]
        return dict(zip(sommetes, voisin))
    
    def ajoutSommet(self, sommet):
        couleur = sommet.getColor()
        
        




    def getGraphSize():
        return __size

