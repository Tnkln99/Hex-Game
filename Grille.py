from tkinter import *
from Hexagon import *
import math

class Grille:

    def __init__(self, size):
        self.__size = size
        self.__matrice = self.__createMatrice(self.__size)
    

    

    def __createMatrice(self, size):
        x0 = 250
        y0 = 250
        M = [[0 for i in range(size)] for j in range(size)]
        M[0][0] = Hexagon(x0,y0,"#FFFFFF")
        for i in range(size):
            for j in range(size):
                if i == 0 and j == 0:
                    continue
                elif j == 0:
                    M[i][j] = Hexagon(M[i-1][j].x[3],M[i-1][j].y[3], "#FFFFFF")
                else:
                    M[i][j] = Hexagon(M[i][j-1].x[2],M[i][j-1].y[2], "#FFFFFF")
        return M


    def getMatrice(self):
        return self.__matrice

    def getSize(self):
        return self.__size






