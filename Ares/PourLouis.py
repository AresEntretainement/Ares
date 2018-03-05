"""
LE but de la classe Error est de capter l'ensemble des bugs du programme et les enregistrer dans un registre log
pour pouvoir apres les analyser et ne pas laisser du code brut trainer.
La classe Error a un initialisateur qui gere directement l'erreur donc pour invoquer une error il suffit juste de 
# CAS OU L'ERREUR EST PARMI CELLES POSSIBLES DANS NOTRE SYSTEME (Casi la majorité des erreurs en gros)

	Temp = Error( ErrorType , ErrorMsg , bSkip , sFileConstants, Vars)

	- Temp est une variable temporaire elle peut avoir n'importe quel nom
	- Error c'est le nom de la classe et elle a 2 PARAMETRES OBLIGATOIRES : ERRORTYPE , ERRORMSG
	- ErrorType: Type d'erreur a afficher et traiter
	 	(ERRORTYPE: Ton but sera de creer au fil et a mesure que tu corriges les classes de 
	 				creer de nouveaux types d'erreurs que tu vas classses dans le ficher 
	 				core/list/listError.py dans le dictionnaire dErrorDictionary, c'est la 
	 				ou il y a les erreurs de notre programe (type: ares_error). Essaye de garder une coherence entre les noms pour avoir differentes familles d'erreurs
	 				Pour les creer essaye de deviner un peu de quoi ca parle la fonction puis avec l'indication que j'ai mis dans le print
	 				et puis tu creeras un message repondant au type d'erreur,  n'hesite pas a me demander)
	 	(PS): Pour trouver toutes les erreurs cherche print dans la barre de recherche de sublime il aura toutes les erreurs j'ai mit un commentaire dessus pour les reconnaitre
	- ErrorMsg : Dans le cas ou tu traites des erreurs de type(arres_error) donc du systeme, le message sera l'enndroit ou tu te trouvers en gros par exemple:
			Dans le fichier (classes.classDatabase):
	l.22			if (~~~~)~:
	l.23				~~~~
	l.24			else:
	l.25				#error
	l.26				print("ERROR DATA BASE IS NOT VALID")
			Tu vas remplacer la partie
					else:
	l.25				#error
	l.26				print("ERROR DATA BASE IS NOT VALID")
			par
				else:
					Temp = Error('NomQueTaurasChoisi' , 'classes.Database.fonctionOuIlYlErreur.25')
					le 25 correpond a la ligne ou il y a l'erreur

	- bSkip : c'est une variable qui prend soit true soit false et qui indique si l'erreur doit etre traité ou pas mais elle sera quand meme entregistré dans le log
	- sFileConstant : c'est la string qui comporte le chemin du fichier log
	- Var : des variables pouvant etre ammenes avec l'erreur et ca sera pour la partie graphique plus tard
LES 3 DERNIERES PARTIES bSkip, sFileConstant et Var ne sont pas a changer donc toutes les erreur auron cette forme
	Temp = Error( ErrorType , ErrorMsg)

# CAS OU L'ERREUR EST PARMI CELLES DU SYSTEME: Il en a pas !

Si t'as un probleme n'hesite pas ;)
je te laisse avec un exemple d'utilisation que tu pouras faire marcher 
######################################
ON TRAVAILLE QUE DANS LE DOSSIER Ares#
######################################



"""

from classes.classError import Error
# 
Temp = Error('Test', 'test12.49')