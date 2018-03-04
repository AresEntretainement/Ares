"""
Algorithme de Boxe IA:


Nous avons defini les types d'exercices specifiques a la boxe qui sont:
-ExerciceWithStrike
-RobotTrain
-RobotTrainSparBar

ExerciceWithStrike:
	Prise d'un seul type de coup,avec plusieurs repetitions lors que c'est indiqué on mesure alors:
		-Force du coup
		-Vitesse du coup
RobotTrain:
	Programme plus complexe utilisant l'ensemble des modules
	{
		Fonctionement:
			Indiquation d'attaques aleatoires d'apres une IA qui releve d'apres une base de données l'ensemble d'enchainements les plus frequents
			On mesure:
			- La force du coup
			- La vitesse du coup
			- Temps de reaction
	}
RobotTrainSparBar:
	Programme de sparring
	{
		Fonctionnement:
			Indiquation d'attaques aleatoires d'apres une IA qui releve d'apres une base de données l'ensemble d'enchainements les plus frequents avec des esquives
			On mesure:
			- La force du coup
			- La vitesse du coup
			- Temps de reaction
			- Capacité d'esquive et de riposte
	}
L'ensemble des informations sont compares avec du big data pour definir un niveau

"""