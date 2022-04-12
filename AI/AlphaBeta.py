from AI import *

# minmax optimisé avec alpha beta

class AlphaBeta(AI):

	def __init__(self,size, color):
		super().__init__(size, color) # appel de classe superieur
		self.name = "AlphaBeta"
		self.PROFONDEUR = 1


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
		if depth == self.PROFONDEUR: # s'il n'y pas de gagnant et on arrive à la limite de profondeur
			return 0


		graphCopyc = Graph(self.size)
		graphCopyc.setGraphR(graph.getGraphR())
		graphCopyc.setGraphB(graph.getGraphB())

		if isMaximizing:
			bestScore = float('-inf')
			for i in range(self.size*self.size):
				if i not in graphCopyc.getGraphComplet():
					graphCopyc.ajoutSommet(self.color, i)
					score = self.alphaBeta(graphCopyc, depth+1, False, alpha, beta)
					bestScore = max(score, bestScore)
					alpha = max(alpha, bestScore)
					if bestScore >= beta:
						break #on coup la branche beta 
			return bestScore

		else:
			bestScore = float('inf')
			for i in range(self.size*self.size):
				if i not in graphCopyc.getGraphComplet():
					graphCopyc.ajoutSommet(rcolor, i)
					score = self.alphaBeta(graphCopyc, depth+1, True, alpha, beta)
					bestScore = min(score, bestScore)
					beta = min(beta, bestScore)
					if bestScore <= alpha:
						break #on coup la branche alpha 
			return bestScore

	def algo(self, GameGraph):
		graphCopy = Graph(self.size)
		graphCopy.setGraphR(GameGraph.getGraphR())
		graphCopy.setGraphB(GameGraph.getGraphB())

		bestScore = float('-inf')
		move = None
		alpha = float('-inf')
		beta = float('inf')


		for i in range(self.size*self.size):
			if i not in graphCopy.getGraphComplet().keys():
				graphCopy.ajoutSommet(self.color, i)
				score = self.alphaBeta(graphCopy, 0, False, alpha, beta)
				if score > bestScore:
					bestScore = score
					move = i

		return move

	

