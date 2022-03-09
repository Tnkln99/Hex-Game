from tkinter import *
from Hexagon import *
import math

class Grille:

    def __init__(self, size):
        self.__size = size
        self.__matrice = self.__createMatrice(self.__size)
    

    

    def __createMatrice(self, size):
        x0 = 60
        y0 = 150
        M = [[0 for i in range(size)] for j in range(size)]
        for i in range(size):
            for j in range(size):
                M[i][j] = Hexagon(x0+i*50*math.sqrt(3)+j*(50/2)*math.sqrt(3) ,y0+j*(50*1.5), "#FFFFFF")
        return M


    def getMatrice(self):
        return self.__matrice

    def getSize(self):
        return self.__size

    def voisinColorCheckForGraph(self, i, j):
        res = []

        if (i == 0): Vkinit = i; Vkfin = i + 1
        elif (i == self.getSize()): Vkfin = i; Vkinit = i - 1
        else: Vkinit = i - 1; Vkfin = i + 1

        
        if (j == 0): Vpinit = j; Vpfin = j + 1
        elif (j == self.getSize()): Vpfin = j; Vpinit = j - 1
        else: Vpinit = j - 1; Vpfin = j + 1

        for k in range(Vkinit,Vkfin):
            for p in range(Vpinit,Vpfin):
                if self.getMatrice()[k][p].getColor() == self.getMatrice()[i][j].getColor():
                    if i == k and j == p:
                        continue
                    res.append(k * self.getSize() + p)
                    
        return res          
            
      





