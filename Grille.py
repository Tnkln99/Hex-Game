from tkinter import *
from Hexagon import *
from Variables import *
import math

class Grille:

    def __init__(self, size):
        self.__size = size
        self.__matrice = self.__createMatrice(self.__size)
    

    
    #tableau pour stocker les positions des centres des hexagones
    def __createMatrice(self, size): 
        self.__tourCount = 0
        x0 = hexL
        y0 = hexL
        M = [[0 for i in range(size)] for j in range(size)]
        for i in range(size):
            for j in range(size):
                M[i][j] = Hexagon(x0+i*hexL*math.sqrt(3)+j*(hexL/2)*math.sqrt(3) ,y0+j*(hexL*1.5))
        return M

    def traceGrille(self, canvasGrille):
        for i in range(self.getSize()):
            for j in range(self.getSize()):
                canvasGrille.create_polygon(self.getMatrice()[i][j].x[0],self.getMatrice()[i][j].y[0],self.getMatrice()[i][j].x[1],self.getMatrice()[i][j].y[1],
                                self.getMatrice()[i][j].x[2],self.getMatrice()[i][j].y[2],self.getMatrice()[i][j].x[3],self.getMatrice()[i][j].y[3],
                                self.getMatrice()[i][j].x[4],self.getMatrice()[i][j].y[4],self.getMatrice()[i][j].x[5],self.getMatrice()[i][j].y[5],
                                fill = self.getMatrice()[i][j].getColor(),
                                outline="#000000")

    def nextTurnHuman(self,event):
        tourCount = self.getTourCount()
        if tourCount % 2 == 0:
            color = "#FF0000"
        else:
            color = "#0000FF"
        if self.trouverClickPoint(event.x,event.y).estLibre():
             self.trouverClickPoint.setColor(color)
             self.tourCountInc()


    def trouverClickPointHuman(self, i, j):
        return M[x][y]


    def getMatrice(self):
        return self.__matrice

    def getSize(self):
        return self.__size

    def getTourCount(self):
        return self.__tourCount

    def tourCountInc(self):
        self.__tourCount += 1




