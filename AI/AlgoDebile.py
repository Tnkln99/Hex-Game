from AI import *


class AlgoDebile(AI):

	def __init__(self,size, color):
		super().__init__(size, color) # appel de classe superieur
		self.name = "AlgoDebile"
		#self.PROFONDEUR = 5



	# Function which finds all the paths
	# and stores it in paths array
	def find_paths(self, paths, path, parent, n, u):
		# Base Case
		if (u == -1):
			paths.append(path.copy())
			return None
 
    	# Loop for all the parents
    	# of the given vertex
		for par in parent[u]:
 
        	# Insert the current
        	# vertex in path
			path.append(u)
 
        	# Recursive call for its parent
			self.find_paths(paths, path, parent, n, par)
 
        	# Remove the current vertex
			path.pop()


	# a modified version of BFS that stores predecessor
	# of each vertex in array p
	# and its distance from source in array d
	def bfs(self, adj, parent, n, start):
		# dist will contain shortest distance
    	# from start to every other vertex
		dist = [1000 for _ in range(n)]
		q = []
 
    	# Insert source vertex in queue and make
    	# its parent -1 and distance 0
		q.append(start)
		parent[start] = [-1]
		dist[start] = 0
 
    # Until Queue is empty
		while q:
			u = q.pop(0)
			if u in adj.keys():
				for v in adj[u]:
					if (dist[v] > dist[u] + 1):
		 
		                # A shorter distance is found
		                # So erase all the previous parents
		                # and insert new parent u in parent[v]
						dist[v] = dist[u] + 1
						q.append(v)
						parent[v].clear()
						parent[v].append(u)

					elif (dist[v] == dist[u] + 1):
		                # Another candidate parent for
		                # shortes path found
						parent[v].append(u)
	                
		     
	    
	         

	# O(V + E)
	def shortestPaths(self, adj, start, end):
		n = self.size * self.size +2
		paths = []
		path = []
		parent = [[] for _ in range(n)]
 
    	# Function call to bfs
		self.bfs(adj, parent, n, start)

    	# Function call to find_paths
		self.find_paths(paths, path, parent, n, end)

		#elmine les sommets invisibles
		for p in paths: 
			p.pop(0)
			p.pop(len(p)-1)

		return paths

	# O((N + M) * T),    T = taille de graphe 
	def extrairChemins(self, GameGraph, cheminCourts1, cheminCourts2, chemins1, chemins2):
		for p in cheminCourts1:
			if self.color == ROUGE:
				for e in GameGraph.getGraphR().keys():
					if e in p:
						chemins1.append(p)
						break
			if self.color == BLUE:
				for e in GameGraph.getGraphB().keys():
					if e in p:
						chemins1.append(p)
						break
		for p in cheminCourts2:
			if self.color == ROUGE:
				for e in GameGraph.getGraphB().keys():
					if e in p:
						chemins2.append(p)
						break
			if self.color == BLUE:
				for e in GameGraph.getGraphR().keys():
					if e in p:
						chemins2.append(p)
						break

	# O(N + M) 
	def intersection(self, intersection, chemins1, chemins2):
		for c1 in chemins1:
			for c2 in chemins2:
				for e in c1:
					if e in c2:
						if e not in intersection:
							intersection.append(e)

	def gagner(self, GameGraph):
		rcolor = None
		if self.color == ROUGE:
			rcolor = BLUE
		else:
			rcolor = ROUGE

		#si il y a une condition gagnant pour nous
		for i in range(self.size * self.size):
			if i not in GameGraph.getGraphComplet():
				GameGraph.ajoutSommet(self.color, i)
				if GameGraph.gagnant(self.color):
					GameGraph.supprimeSommet(self.color, i)
					return i
				GameGraph.supprimeSommet(self.color, i)

		#si il y a une condition gagnant pour adversaire on empeche
		for i in range(self.size * self.size):
			if i not in GameGraph.getGraphComplet():
				GameGraph.ajoutSommet(rcolor, i)
				if GameGraph.gagnant(rcolor):
					GameGraph.supprimeSommet(rcolor, i)
					return i
				GameGraph.supprimeSommet(rcolor, i)


	# alpha beta algorithme entres les intersection
	def ab(self, graph, depth, isMaximizing, alpha, beta):
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

		#self.gagner(graph)
		
		# copie de graph de jeu
		GraphCopy1 = Graph(self.size)
		GraphCopy1.setGraphR(graph.getGraphR())
		GraphCopy1.setGraphB(graph.getGraphB())

		GraphCopy2 = Graph(self.size)
		GraphCopy2.setGraphR(graph.getGraphR())
		GraphCopy2.setGraphB(graph.getGraphB())


		# on remplit la graphe avec la couleur de IA et l'autre avec couleur d'adversaire
		for i in range(self.size * self.size):
			if i not in GraphCopy1.getGraphComplet():
				GraphCopy1.ajoutSommet(self.color, i)
			if i not in GraphCopy2.getGraphComplet():
				GraphCopy2.ajoutSommet(rcolor, i)

		# sommets invisibles
		Sa = self.size*self.size 
		Sb = self.size*self.size +1 

		cheminCourts1 = None
		cheminCourts2 = None

		if self.color == ROUGE:
			cheminCourts1 = self.shortestPaths(GraphCopy1.getGraphR(), Sa, Sb)
			cheminCourts2 = self.shortestPaths(GraphCopy2.getGraphB(), Sa, Sb)
		if self.color == BLUE:
			cheminCourts1 = self.shortestPaths(GraphCopy1.getGraphB(), Sa, Sb)
			Sa = self.size*self.size 
			Sb = self.size*self.size +1 
			cheminCourts2 = self.shortestPaths(GraphCopy2.getGraphR(), Sa, Sb)


		# etape 2: entre les chemins on exraire les chemins qui contients deja ces sommets dans le graph
		chemins1 = []
		chemins2 = []
		self.extrairChemins(graph, cheminCourts1, cheminCourts2, chemins1, chemins2)

		# etape 3: on extraire les chemin qui contient la même coup pour 2 jouers
		# intersection des coups
		intersection = []
		self.intersection(intersection, chemins1, chemins2)


		if isMaximizing:
			bestScore = float('-inf')
			for i in intersection:
				if i not in graph.getGraphComplet():
					graph.ajoutSommet(self.color, i)
					score = self.ab(graph, depth+1, False, alpha, beta)
					graph.supprimeSommet(self.color, i)
					bestScore = max(score, bestScore)
					alpha = max(alpha, bestScore)
					if alpha >= beta:
						break #on coup la branche beta 
			return bestScore

		else:
			bestScore = float('inf')
			for i in intersection:
				if i not in graph.getGraphComplet():
					graph.ajoutSommet(rcolor, i)
					score = self.ab(graph, depth+1, True, alpha, beta)
					graph.supprimeSommet(rcolor, i)
					bestScore = min(score, bestScore)
					beta = min(beta, bestScore)
					if beta <= alpha:
						break #on coup la branche alpha 
			return bestScore



	def algo(self, GameGraph):
		tour = len(GameGraph.getGraphComplet().keys()) -2
		rcolor = None
		if self.color == ROUGE:
			rcolor = BLUE
		else:
			rcolor = ROUGE


		if self.center not in GameGraph.getGraphComplet():
			return self.center

		#si il y a une condition gagnant pour nous
		for i in range(self.size * self.size):
			if i not in GameGraph.getGraphComplet():
				GameGraph.ajoutSommet(self.color, i)
				if GameGraph.gagnant(self.color):
					GameGraph.supprimeSommet(self.color, i)
					return i
				GameGraph.supprimeSommet(self.color, i)

		#si il y a une condition gagnant pour adversaire on empeche
		for i in range(self.size * self.size):
			if i not in GameGraph.getGraphComplet():
				GameGraph.ajoutSommet(rcolor, i)
				if GameGraph.gagnant(rcolor):
					GameGraph.supprimeSommet(rcolor, i)
					return i
				GameGraph.supprimeSommet(rcolor, i)

		# copie de graph de jeu
		GraphCopy1 = Graph(self.size)
		GraphCopy1.setGraphR(GameGraph.getGraphR())
		GraphCopy1.setGraphB(GameGraph.getGraphB())

		GraphCopy2 = Graph(self.size)
		GraphCopy2.setGraphR(GameGraph.getGraphR())
		GraphCopy2.setGraphB(GameGraph.getGraphB())


		# on remplit la graphe avec la couleur de IA et l'autre avec couleur d'adversaire
		for i in range(self.size * self.size):
			if i not in GraphCopy1.getGraphComplet():
				GraphCopy1.ajoutSommet(self.color, i)
			if i not in GraphCopy2.getGraphComplet():
				GraphCopy2.ajoutSommet(rcolor, i)

		# sommets invisibles
		Sa = self.size*self.size 
		Sb = self.size*self.size +1 

		cheminCourts1 = None
		cheminCourts2 = None

		if self.color == ROUGE:
			cheminCourts1 = self.shortestPaths(GraphCopy1.getGraphR(), Sa, Sb)
			cheminCourts2 = self.shortestPaths(GraphCopy2.getGraphB(), Sa, Sb)
		if self.color == BLUE:
			cheminCourts1 = self.shortestPaths(GraphCopy1.getGraphB(), Sa, Sb)
			Sa = self.size*self.size 
			Sb = self.size*self.size +1 
			cheminCourts2 = self.shortestPaths(GraphCopy2.getGraphR(), Sa, Sb)


		# etape 2: entre les chemins on exraire les chemins qui contients deja ces sommets dans le graph
		chemins1 = []
		chemins2 = []
		self.extrairChemins(GameGraph, cheminCourts1, cheminCourts2, chemins1, chemins2)

		# etape 3: on extraire les chemin qui contient la même coup pour 2 jouers
		# intersection des coups
		intersection = []
		self.intersection(intersection, chemins1, chemins2)

		#etape 4: 
		if intersection:
			x = random.randint(0, len(intersection)-1)
			return intersection[x]
		elif chemins2:
			x = random.randint(0, len(chemins2)-1)
			y = random.randint(0, len(chemins2[x])-1)
			move = chemins2[x][y]
			while move in GameGraph.getGraphComplet().keys():
				x = random.randint(0, len(chemins2)-1)
				y = random.randint(0, len(chemins2[x])-1)
			move = chemins2[x][y]
			return chemins2[x][y]
		else:
			x = random.randint(0, self.size*self.size-1)
			while x in GameGraph.getGraphComplet().keys():
				x = random.randint(0, self.size*self.size-1)

			return x
		"""bestScore = float('-inf')
		move = None
		alpha = float('-inf')
		beta = float('inf')

		for i in intersection:
			GameGraph.ajoutSommet(self.color, i)
			score = self.ab(GameGraph, 0, False, alpha, beta)
			GameGraph.supprimeSommet(self.color, i)
			if score > bestScore:
				bestScore = score
				move = i


		return move"""

		