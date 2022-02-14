from tkinter import *
import math

class Hexagon:

    def __init__(self, x0, y0, color):
        self.x = []
        self.y = []
        for i in range(6) :
            angle = math.radians(i*360/6)
            self.x.append(int(x0+50*math.cos(angle)))
            self.y.append(int(y0+50*math.sin(angle)))
        self.__color = color

    def getColor(self):
        return self.__color
 






