from Grille import *
from tkinter import *


FirstGrille = Grille(4)

Window = Tk()
Window.title("Hex Game")
Window.geometry("1000x1000")
Window.config(background='#FFFFFF')


myCanvas = Canvas(Window, width=500, height=500, bg="#FFFFFF")
myCanvas.pack(pady = 100)

for i in range(FirstGrille.getSize()):
    for j in range(FirstGrille.getSize()):
        myCanvas.create_polygon(FirstGrille.getMatrice()[i][j].x[0],FirstGrille.getMatrice()[i][j].y[0],FirstGrille.getMatrice()[i][j].x[1],FirstGrille.getMatrice()[i][j].y[1],
                                FirstGrille.getMatrice()[i][j].x[2],FirstGrille.getMatrice()[i][j].y[2],FirstGrille.getMatrice()[i][j].x[3],FirstGrille.getMatrice()[i][j].y[3],
                                FirstGrille.getMatrice()[i][j].x[4],FirstGrille.getMatrice()[i][j].y[4],FirstGrille.getMatrice()[i][j].x[5],FirstGrille.getMatrice()[i][j].y[5],
                                fill = FirstGrille.getMatrice()[i][j].getColor(),
                                outline="#000000")
        print("x1= ",FirstGrille.getMatrice()[i][j].x[0],"y1= ",FirstGrille.getMatrice()[i][j].y[0],"x2 =",FirstGrille.getMatrice()[i][j].x[1],"y2= ",FirstGrille.getMatrice()[i][j].y[1],
              "x3= ",FirstGrille.getMatrice()[i][j].x[2],"y3= ",FirstGrille.getMatrice()[i][j].y[2],"x4= ",FirstGrille.getMatrice()[i][j].x[3],"y4= ",FirstGrille.getMatrice()[i][j].y[3],
              "x5= ",FirstGrille.getMatrice()[i][j].x[4],"y5= ",FirstGrille.getMatrice()[i][j].y[4],"x6= ",FirstGrille.getMatrice()[i][j].x[5],"y6 =",FirstGrille.getMatrice()[i][j].y[5])
        print("\n")
      
       



Window.mainloop()




