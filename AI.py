import random

class AI:

	def __init__(self, size, grapheR, grapheB):
		self.GrapheComplet = {**grapheR, **grapheB}  # combine 2 graphe dans une seule graphe
		self.size = size

	def algo:
		printf("Cette fonction serre à rien car c'est la classe abstract")
		

class AlgoRandom(AI):

	def __init__(self,size, grapheR, grapheB):
		super.__init__(size, grapheR, grapheB) # appel de classe superieur

	def algoRandom(self):
		x = random.randint(0, self.size*self.size-1)
		while x in self.GrapheComplet.keys():
			x = random.randint(0, self.size*self.size-1)

		return x


class AlgoS(AI):

	def __init__(self,size, grapheR, grapheB, color):
		super.__init__(size, grapheR, grapheB) # appel de classe superieur

		self.color = color

	def algo:



    
