from AI import *

class AlgoRandom(AI):

	def __init__(self,size, grapheR, grapheB, color):
		super().__init__(size, grapheR, grapheB, color) # appel de classe superieur

	def algo(self):
		x = random.randint(0, self.size*self.size-1)
		while x in self.GrapheComplet.keys():
			x = random.randint(0, self.size*self.size-1)

		return x
