
"""
Cherche dans le ficher core.classes l'ensemble des 
0"""	

def class_exist(sClass):
	from list.listClass import aDictionnaryClasses
	if (sClass in aDictionnaryClasses):
		return True
	else:
		return False
