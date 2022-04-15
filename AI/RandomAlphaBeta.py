from AI import *


# minmax optimisé avec alpha beta

class RandomAlphaBeta(AI):

	def __init__(self,size, color):
		super().__init__(size, color) # appel de classe superieur
		self.name = "Random AlphaBeta"
		self.possibilite = self.size * self.size


	def setPossibilite(self, x):
		self.possibilite = x

	def getPossibilite(self):
		return self.possibilite


	def alphaBeta(self, graph, depth, isMaximizing, alpha, beta):
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

		tour = len(graph.getGraphComplet().keys()) -2
		if self.size*self.size - tour == self.getPossibilite()-1:
			self.setPossibilite(self.getPossibilite()-1)


		poss = []

		for i in range(self.possibilite):
			x = random.randint(0, self.size*self.size-1)
			while x in graph.getGraphComplet().keys():
				x = random.randint(0, self.size*self.size-1)

			if x not in poss:
				poss.append(x)
			else:
				i-=1


		if isMaximizing:
			bestScore = float('-inf')
			for i in poss:
				if i not in graph.getGraphComplet():
					graph.ajoutSommet(self.color, i)
					score = self.alphaBeta(graph, depth+1, False, alpha, beta)
					graph.supprimeSommet(self.color, i)
					bestScore = max(score, bestScore)
					alpha = max(alpha, bestScore)
					if alpha >= beta:
						break #on coup la branche beta 
			return bestScore

		else:
			bestScore = float('inf')
			for i in poss:
				if i not in graph.getGraphComplet():
					graph.ajoutSommet(rcolor, i)
					score = self.alphaBeta(graph, depth+1, True, alpha, beta)
					graph.supprimeSommet(rcolor, i)
					bestScore = min(score, bestScore)
					beta = min(beta, bestScore)
					if beta <= alpha:
						break #on coup la branche alpha 
			return bestScore

	def algo(self, GameGraph):

		bestScore = float('-inf')
		move = None
		alpha = float('-inf')
		beta = float('inf')

		tour = len(GameGraph.getGraphComplet().keys()) -2
		if self.size*self.size - tour == self.getPossibilite()-1:
			self.setPossibilite(self.getPossibilite()-1)


		poss = []

		for i in range(self.possibilite):
			x = random.randint(0, self.size*self.size-1)
			while x in GameGraph.getGraphComplet().keys():
				x = random.randint(0, self.size*self.size-1)

			if x not in poss:
				poss.append(x)
			else:
				i-=1

		for i in poss:
			if i not in GameGraph.getGraphComplet().keys():
				GameGraph.ajoutSommet(self.color, i)
				score = self.alphaBeta(GameGraph, 0, False, alpha, beta)
				GameGraph.supprimeSommet(self.color, i)
				if score > bestScore:
					bestScore = score
					move = i


		return move

	



	