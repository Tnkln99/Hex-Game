from Grille import *
from tkinter import *
from Graph import *
#from Functions import *


class Jeu:
    
    def __init__(self):
        self.__turnCount = 0

        self.Window = Tk()
        self.Window.title("Hex Game")
        self.Window.geometry("1000x1000")
        self.Window.config(background='#FFFFFF')

        self.myCanvas = Canvas(self.Window, width=1100, height=1100, bg="#FFFFFF")
        self.myCanvas.pack(pady = 100)

        self.commencer(self.myCanvas,self.Window, self.getTurnCount())

          
    def commencer(self, canvas, windows, turnCount):
        self.size = 6

        self.notreGraph = Graph(self.size) # initialize de graphe

        self.FirstGrille = Grille(self.size, self.myCanvas)
        self.FirstGrille.traceGrille(self.myCanvas)

        self.myCanvas.bind("<Button-1>", self.nextTurnHuman)

        self.Window.mainloop()

    def nextTurnHuman(self,event):
        color = ""
        if self.getTurnCount() % 2 == 0:
            color = "#FF0000"
        else:
            color = "#0000FF"
        #Récuperation des points cliqée
        pointCliquee = event.x, event.y
        #trouver la hexagone associée aux points
        hexagonCliquee = self.trouverHexagonCliqueHuman(pointCliquee)
        if hexagonCliquee[0]:
            hexCliquee = hexagonCliquee[1]
            pointIetJ = hexagonCliquee[2]
            if hexCliquee.estLibre():
                hexCliquee.changeColor(self.myCanvas, color)
                self.incTurnCount()
                self.notreGraph.ajoutSommet(color, pointIetJ) 
                print(self.notreGraph.getGraphR())
                #self.nextTurn()

        if self.notreGraph.gagnantR():
            print("rouge a gagné ")
            # aret de jeu 
        if self.notreGraph.gagnantB():
            print("blue a gagné ")
            # aret de jeu 
                
        
    #trouver la hexagone associée aux points cliquées
    def trouverHexagonCliqueHuman(self, p):
        for i in range(self.FirstGrille.getSize()):
            for j in range(self.FirstGrille.getSize()):
                if self.FirstGrille.getMatrice()[i][j].distance(p) <= hexL:
                    x = j * self.FirstGrille.getSize() + i
                    return True, self.FirstGrille.getMatrice()[i][j], x
        return False, None, (-1, -1)

    def incTurnCount(self):
        self.__turnCount += 1

    def getTurnCount(self):
        return self.__turnCount

    def winCond(self, graph):
        return True




Jeu()
    


        

      





