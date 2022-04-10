from AI import *

class AlgoRandom(AI):

	def __init__(self,size, color):
		super().__init__(size, color) # appel de classe superieur

		self.name = "RandomAI"

	def algo(self, GameGraph):

		x = random.randint(0, self.size*self.size-1)
		while x in GameGraph.getGraphComplet().keys():
			x = random.randint(0, self.size*self.size-1)

		return x
