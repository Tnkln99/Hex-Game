from AI import *



class MinMax(AI):

	def __init__(self,size, color):
		super().__init__(size, color) # appel de classe superieur
		self.name = "MinMax"


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

		if isMaximizing:
			bestScore = float('-inf')
			for i in range(self.size*self.size):
				if i not in graphCopyc.getGraphComplet():
					graphCopyc.ajoutSommet(self.color, i)
					score = self.minmax(graphCopyc, depth+1, False)
					bestScore = max(score, bestScore)
			return bestScore

		else:
			bestScore = float('inf')
			for i in range(self.size*self.size):
				if i not in graphCopyc.getGraphComplet():
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


		for i in range(self.size*self.size):
			if i not in graphCopy.getGraphComplet().keys():
				graphCopy.ajoutSommet(self.color, i)
				score = self.minmax(graphCopy, 0, False)
				if score > bestScore:
					bestScore = score
					move = i

		return move

	






"""
*********************************************************

	def minmax(position, depth, maximizingPlayer):
		if depth == 0: # + or game over in postion
			return position

		if maximizingPlayer:
			maxEval = float('-inf')

			for each child of position:
				eval = minmax(child, depth - 1, false)
				maxEval = max(maxEval, eval)

			return maxEval

		else: 
			minEval = float('inf')

			for each child of position:
				eval = minmax(child, depth - 1, true)
				minEval = min(minEval, eval)

			return minEval
"""