from tkinter import *
from Variables import *
import math

class Hexagon:

    def __init__(self, x0, y0):
        self.x = []
        self.y = []
        # calculer les 6 sommetes d'une hexagione à partir de son centre
        for i in range(6) :
            angle = math.radians(i*360/6)
            self.x.append(int(x0+hexL*math.sin(angle)))
            self.y.append(int(y0+hexL*math.cos(angle)))

        self.__color = "#FFFFFF"


    # Getters et Setters

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def setValue(self, value):
        self.__value = value

    def estLibre():
        if self.getColor() == "#FFFFFF":
            return True
        return False






