from Grille import *
from tkinter import *
from Graph import *
#from Functions import *


class Jeu:
    
    def __init__(self):
        self.__turnCount = 0
        
        self.menu()

        self.Window = Tk()
        self.Window.title("Hex Game")
        self.Window.geometry("1000x1000")
        self.Window.config(background='#FFFFFF')

        self.myCanvas = Canvas(self.Window, width=1100, height=1100, bg="#FFFFFF")
        self.myCanvas.pack(pady = 100)

        self.commencer(self.myCanvas,self.Window, self.getTurnCount())

          
    def commencer(self, canvas, windows, turnCount):
        self.size = 6

        self.notreGraph = Graph(self.size) # initialize de graphe

        self.FirstGrille = Grille(self.size, self.myCanvas)
        self.FirstGrille.traceGrille(self.myCanvas)

        self.myCanvas.bind("<Button-1>", self.nextTurnHuman)

        self.Window.mainloop()

    def nextTurnHuman(self,event):
        color = ""
        if self.getTurnCount() % 2 == 0:
            color = "#FF0000"
        else:
            color = "#0000FF"
        #Récuperation des points cliqée
        pointCliquee = event.x, event.y
        #trouver la hexagone associée aux points
        hexagonCliquee = self.trouverHexagonCliqueHuman(pointCliquee)
        if hexagonCliquee[0]:
            hexCliquee = hexagonCliquee[1]
            pointIetJ = hexagonCliquee[2]
            if hexCliquee.estLibre():
                hexCliquee.changeColor(self.myCanvas, color)
                self.incTurnCount()
                self.notreGraph.ajoutSommet(color, pointIetJ) 
        if self.notreGraph.gagnantR():
            print("rouge a gagné ")
            self.Window.destroy()
        if self.notreGraph.gagnantB():
            print("blue a gagné ")
            self.Window.destroy()
                
        
    #trouver la hexagone associée aux points cliquées
    def trouverHexagonCliqueHuman(self, p):
        for i in range(self.FirstGrille.getSize()):
            for j in range(self.FirstGrille.getSize()):
                if self.FirstGrille.getMatrice()[i][j].distance(p) <= hexL:
                    x = j * self.FirstGrille.getSize() + i
                    return True, self.FirstGrille.getMatrice()[i][j], x
        return False, None, (-1, -1)

    def incTurnCount(self):
        self.__turnCount += 1

    def getTurnCount(self):
        return self.__turnCount
    
    def menu(self):
        fenetreMenu = Tk(className='configuration')
        fenetreMenu.resizable(width=False, height=False)
        fenetreMenu.geometry('520x500+700+300')
        
        FrameNomFichier = Frame(fenetreMenu,pady=10,padx=10)
        texteNomFichier = Label(FrameNomFichier, text="Nom d'Enregistrement : ", font="Arial 15")
        texteNomFichier.pack(side='left')
        fichier = Text(FrameNomFichier,font="Arial 15",width=15,height=1)
        fichier.pack(side='right')
        FrameNomFichier.pack()

        FrameTaille = Frame(fenetreMenu,pady=10,padx=10)
        texteTaille = Label(FrameTaille, text="Taille : ", font="Arial 15")
        texteTaille.pack(side='left')
        taille = Spinbox(FrameTaille,from_=2, to=11,font="Arial 15",width=15)
        taille.pack(side='right')
        FrameTaille.pack()
        

        FrameJoueur = Frame(fenetreMenu,pady=10)
        Frame1 = Frame(FrameJoueur)
        choix1 = [("Joueur","Joueur"),("IA","IA")]

        texteJoueur1 = Label(Frame1,text="Joueur 1 : ",fg='#FF0000', font="Arial 15")
        texteJoueur1.pack(side='left')

        choix1 = [("Joueur",0),("IA",1)]
        var1 = StringVar()
        for text, val in choix1 :
            rb = Radiobutton(Frame1, text=text, variable=var1, value=val, font="Arial 15")
            # valeur par defaut : joueur 1 IA
            if (val == 1):
                rb.select()
            rb.pack(side='right')
        Frame1.pack()

        Frame2 = Frame(FrameJoueur, pady=10)
        texteJoueur2 = Label(Frame2,text="Joueur 2 : ", fg='#0000FF',font="Arial 15")
        texteJoueur2.pack(side='left')

        choix2 = [("Joueur",0),("IA",1)]
        var2 = StringVar()
        for text, val in choix2:
            rb2 = Radiobutton(Frame2, text=text, variable=var2, value=val, font="Arial 15")
            # valeur par defaut : joueur 2 Joueur
            if (val == 0):
                rb2.select()
            rb2.pack(side='right')
        Frame2.pack()
        FrameJoueur.pack()

        b = Button(fenetreMenu,text="Jouer",command=lambda: self.enregistreJeu(fichier.get()))
        b.pack()
        

    def enregistreJeu(self, nomFichier):
        return "cliqué"
    
    




Jeu()
    


        

      





