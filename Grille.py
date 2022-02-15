from tkinter import *
from Hexagon import *
import math

class Grille:

    def __init__(self, size):
        self.__size = size
        self.__matrice = self.__createMatrice(self.__size)
    

    

    def __createMatrice(self, size):
        x0 = 50
        y0 = 50
        M = [[0 for i in range(size)] for j in range(size)]
        for i in range(size):
            for j in range(size):
                M[i][j] = Hexagon(x0+i*50*math.sqrt(3)+j*(50/2)*math.sqrt(3) ,y0+j*(50*1.5), "#FFFFFF")
        return M


    def getMatrice(self):
        return self.__matrice

    def getSize(self):
        return self.__size






