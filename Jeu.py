from Grille import *
from tkinter import *
#from Functions import *


class Jeu:

    def __init__(self):
        self.size = 6
        self.Window = Tk()
        self.Window.title("Hex Game")
        self.Window.geometry("1000x1000")
        self.Window.config(background='#FFFFFF')


        self.myCanvas = Canvas(self.Window, width=1100, height=1100, bg="#FFFFFF")
        self.myCanvas.pack(pady = 100)

        self.FirstGrille = Grille(self.size, self.myCanvas)
        self.FirstGrille.traceGrille(self.myCanvas)

        self.myCanvas.bind("<Button-1>", self.nextTurnHuman)


        self.Window.mainloop()

        


    def nextTurnHuman(self,event):
        tourCount = self.FirstGrille.getTourCount()
        color = ""
        if tourCount % 2 == 0:
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
                self.FirstGrille.tourCountInc()

        
             

    #trouver la hexagone associée aux points cliquées
    def trouverHexagonCliqueHuman(self, p):
        for i in range(self.FirstGrille.getSize()):
            for j in range(self.FirstGrille.getSize()):
                if self.FirstGrille.getMatrice()[i][j].distance(p) <= hexL:
                    return True, self.FirstGrille.getMatrice()[i][j]
        return False, None

Jeu()
    


        

      





