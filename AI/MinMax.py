from AI import *

class MinMax(AI):

	def __init__(self,size, grapheR, grapheB, color):
		super().__init__(size, grapheR, grapheB, color) # appel de classe superieur

	def algo(self):
		return x


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