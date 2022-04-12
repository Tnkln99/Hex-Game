import random

import sys
sys.path.append('../')

from Graph import *

class AI:

	def __init__(self, size, color): # color pour voir 
		self.name = None
		self.color = color
		self.size = size
		self.center = int((self.size * self.size)/2)

	def algo(self, GameGraph):
		raise NotImplementedError("""Cette fonction serre à rien car c'est la classe abstract
				  si vous voulez implementer votre propre AI créez une nouvelle fichier dans le dossier AI 
				  cette AI devrait être herité de class AI avec une method 'algo' qui renvoit la valeur
				  de case choisi puis vous pouvez selectioner votre algo par le menu de configuraation. """)
		
