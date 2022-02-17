from tkinter import *
from Hexagon import *
from variables import *
import math

class Grille:

    def __init__(self, size):
        self.__size = size
        self.__matrice = self.__createMatrice(self.__size)
    

    
    #tableau pour stocker les positions des centres des hexagones
    def __createMatrice(self, size): 
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


    def getMatrice(self):
        return self.__matrice

    def getSize(self):
        return self.__size






