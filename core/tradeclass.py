
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

"""
Cherche dans le ficher core.classes l'ensemble des classes
0"""	

def class_exist(sClass):
	from list.listClass import aDictionnaryClasses
	if (sClass in aDictionnaryClasses):
		return True
	else:
		return False
