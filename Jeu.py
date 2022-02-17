from Grille import *
from tkinter import *
#from Functions import *

    

size = 4



Window = Tk()
Window.title("Hex Game")
Window.geometry("1000x1000")
Window.config(background='#FFFFFF')


myCanvas = Canvas(Window, width=1000, height=1000, bg="#FFFFFF")
myCanvas.pack(pady = 100)

FirstGrille = Grille(size, myCanvas)

FirstGrille.traceGrille(myCanvas)

myCanvas.bind("<Button-1>", FirstGrille.nextTurnHuman)


        

      
Window.mainloop()




