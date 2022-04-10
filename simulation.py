# simulation des algorithmes
from Variables import *

import matplotlib.pyplot as plt
import sys
sys.path.append('AI')
from RandomAI import *
from MinMax import *

def ploting(AI1, AI2, statistic):
	plt.figure("jeu en temps", figsize=(12,6))

	numeroJeu = [i for i in range(1, len(statistic)+1)]

	plt.plot(numeroJeu, statistic) 

	plt.title(AI1.name + " vs " + AI2.name)

	plt.xlabel("Numéro de Jeu")

	plt.ylabel(" gagnant 0 si AI1 1 si AI2")


	# 2ème plot
	plt.figure("proportion de condition gagner")

	nbrGagneAI1 = statistic.count(0)
	nbrGagneAI2 = statistic.count(1)
	y = [nbrGagneAI1, nbrGagneAI2]
	names = [AI1.name, AI2.name]

	plt.pie(y, labels = names, autopct='%1.2f%%')


	plt.show()

def simulation(AI1, AI2, nombreJeu, size):

	# 0 si AI1 gagne
	# 1 si AI2 gagne

	statistic = [-1 for i in range(int(nombreJeu/2)*2)]

	for i in range(0, int(nombreJeu/2)*2, 2):
		GameGraph = Graph(size)

		while True:
			a = AI1.algo(GameGraph)
			GameGraph.ajoutSommet(ROUGE, a)
			if GameGraph.gagnant(ROUGE):
				statistic[i] = 0
				print("rouge a gagné")
				break

			a = AI2.algo(GameGraph)
			GameGraph.ajoutSommet(BLUE, a)
			if GameGraph.gagnant(BLUE):
				statistic[i] = 1
				print("blue a gagné")
				break

		# ici on change l'AI qui commence en premier 
		# donc pas d'avantage pour le AI qui commence en premier

		GameGraph = Graph(size)

		while True:
			a = AI2.algo(GameGraph)
			GameGraph.ajoutSommet(BLUE, a)
			if GameGraph.gagnant(BLUE):
				statistic[i+1] = 1
				print("blue a gagné")
				break

			a = AI1.algo(GameGraph)
			GameGraph.ajoutSommet(ROUGE, a)
			if GameGraph.gagnant(ROUGE):
				statistic[i+1] = 0
				print("rouge a gagné")
				break

	ploting(AI1, AI2, statistic)




nombreJeu = 100
size = 11

AI1 = AlgoRandom(size, ROUGE)
AI2 = MinMax(size, BLUE)

simulation(AI1, AI2, nombreJeu, size)
