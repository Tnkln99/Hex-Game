from AI import *


class RandomMinMax(AI):

	def __init__(self,size, color):
		super().__init__(size, color) # appel de classe superieur
		self.name = "RandomMinMax"
		self.possibilite = 2
		


	def minmax(self, graph, depth, isMaximizing):
		#controler les condition gagnants
		rcolor = None
		if self.color == ROUGE:
			rcolor = BLUE
		else:
			rcolor = ROUGE
			
		if graph.gagnant(self.color):
			return 1
		if graph.gagnant(rcolor):
			return -1

		graphCopyc = Graph(self.size)
		graphCopyc.setGraphR(graph.getGraphR())
		graphCopyc.setGraphB(graph.getGraphB())

		poss = []

		for i in range(self.possibilite):
			x = random.randint(0, self.size*self.size-1)
			while x in graphCopyc.getGraphComplet().keys():
				x = random.randint(0, self.size*self.size-1)

			if x not in poss:
				poss.append(x)
			else:
				i-=1

		if isMaximizing:
			bestScore = float('-inf')
			for i in poss:
				graphCopyc.ajoutSommet(self.color, i)
				score = self.minmax(graphCopyc, depth+1, False)
				bestScore = max(score, bestScore)
			return bestScore

		else:
			bestScore = float('inf')
			for i in poss:
				graphCopyc.ajoutSommet(rcolor, i)
				score = self.minmax(graphCopyc, depth+1, True)
				bestScore = min(score, bestScore)
			return bestScore

	def algo(self, GameGraph):

		graphCopy = Graph(self.size)
		graphCopy.setGraphR(GameGraph.getGraphR())
		graphCopy.setGraphB(GameGraph.getGraphB())

		bestScore = float('-inf')
		move = None

		poss = []

		for i in range(self.possibilite):
			x = random.randint(0, self.size*self.size-1)
			while x in GameGraph.getGraphComplet().keys():
				x = random.randint(0, self.size*self.size-1)

			if x not in poss:
				poss.append(x)
			else:
				i-=1

		print(len(poss))


		for i in poss:
			graphCopy.ajoutSommet(self.color, i)
			score = self.minmax(graphCopy, 0, False)
			if score > bestScore:
				bestScore = score
				move = i

		return move
	





