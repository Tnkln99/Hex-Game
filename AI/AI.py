import random

import sys
sys.path.append('../')

from Graph import *

class AI:

	def __init__(self, size, grapheR, grapheB, color): # color pour voir 
		self.graphAI = Graph(size)
		self.graphAI.setGraphR(grapheR)
		self.graphAI.setGraphB(grapheB)
		self.GrapheComplet = {**self.graphAI.getGraphR(), **self.graphAI.getGraphB()}  # combine 2 graphe dans une seule graphe
		self.color = color
		self.size = size

	def algo(self):
		raise NotImplementedError("""Cette fonction serre à rien car c'est la classe abstract
				  si vous voulez implementer votre propre AI créez une nouvelle fichier dans le dossier AI 
				  cette AI devrait être herité de class AI avec une method 'algo' qui renvoit la valeur
				  de case choisi puis vous pouvez selectioner votre algo par le menu de configuraation. """)
		



    
