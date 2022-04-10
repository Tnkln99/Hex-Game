
import random

import sys
sys.path.append('../')

from Graph import *

class AIs:

	def __init__(self, size, grapheR, grapheB, color): # color pour voir 
		self.graphAI = Graph(size)
		self.graphAI.setGraphR(grapheR)
		self.graphAI.setGraphB(grapheB)
		self.GrapheComplet = {**self.graphAI.getGraphR(), **self.graphAI.getGraphB()}  # combine 2 graphe dans une seule graphe
		self.color = color
		self.size = size

	
a = AIs(10)

a.x = 20

print(a.t)


