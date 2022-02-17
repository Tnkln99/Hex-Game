from Grille import *
from tkinter import *

size = 4

FirstGrille = Grille(size)

Window = Tk()
Window.title("Hex Game")
Window.geometry("1000x1000")
Window.config(background='#FFFFFF')


myCanvas = Canvas(Window, width=1000, height=1000, bg="#FFFFFF")
myCanvas.pack(pady = 100)


FirstGrille.traceGrille(myCanvas)
        

      
       



Window.mainloop()




