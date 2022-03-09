from Grille import *
#from Graph import *
from tkinter import *


FirstGrille = Grille(4)

Window = Tk()
Window.title("Hex Game")
Window.geometry("1000x1000")
Window.config(background='#FFFFFF')


myCanvas = Canvas(Window, width=500, height=500, bg="#FFFFFF")
myCanvas.pack(pady = 100)

for i in range(FirstGrille.getSize()):
    for j in range(FirstGrille.getSize()):
        myCanvas.create_polygon(FirstGrille.getMatrice()[i][j].x[0],FirstGrille.getMatrice()[i][j].y[0],FirstGrille.getMatrice()[i][j].x[1],FirstGrille.getMatrice()[i][j].y[1],
                                FirstGrille.getMatrice()[i][j].x[2],FirstGrille.getMatrice()[i][j].y[2],FirstGrille.getMatrice()[i][j].x[3],FirstGrille.getMatrice()[i][j].y[3],
                                FirstGrille.getMatrice()[i][j].x[4],FirstGrille.getMatrice()[i][j].y[4],FirstGrille.getMatrice()[i][j].x[5],FirstGrille.getMatrice()[i][j].y[5],
                                fill = FirstGrille.getMatrice()[i][j].getColor(),
                                outline="#000000")
      
       

        #self.Graph = Graph(self.size)

        self.myCanvas.bind("<Button-1>", self.nextTurnHuman)


    def nextTurnHuman(self,event):
        color = ""
        if self.getTurnCount() % 2 == 0:
            color = "#FF0000"
        else:
            color = "#0000FF"
        #Récuperation des points cliqée
        pointCliquee = event.x, event.y
        #trouver la hexagone associée aux points
        if self.trouverHexagonCliqueHuman(pointCliquee)[0]:
            hexCliquee = self.trouverHexagonCliqueHuman(pointCliquee)[1]
            if hexCliquee.estLibre():
                hexCliquee.changeColor(self.myCanvas, color)
                self.incTurnCount()
        
    #trouver la hexagone associée aux points cliquées
    def trouverHexagonCliqueHuman(self, p):
        for i in range(self.FirstGrille.getSize()):
            for j in range(self.FirstGrille.getSize()):
                if self.FirstGrille.getMatrice()[i][j].distance(p) <= hexL:
                    return True, self.FirstGrille.getMatrice()[i][j]
        return False, None

    def incTurnCount(self):
        self.__turnCount += 1

    def getTurnCount(self):
        return self.__turnCount




Jeu()
    


        

      





