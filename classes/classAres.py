# -*-coding:utf-8 -*-
"""[ARES CLASS]

[description]
ARES CLASS : Toutes les interactions sont 
executés via cette classe.
C'est le premier objet qui sera crée lors de
l'initalisation
$id = /include/library/ares/classAres.py
"""


"""
	IMPORTATION
"""

import sys
from hashlib import md5


"""
CONSTANTS

"""

#sys.path[:0] = ['../']


from constants import *
from core.serialize import *
from core.tradeclass import * 
from .classError import *


def defined(constant):
	if constant != True:
		exit()
	return 



"""
 * @copyright		[ARES ENTRETAINEMENT]
 * @author			CHOUBIKI Ismael	
 * @package 		AresTrain
 * @version 		$Id: classAres.py
"""


class Ares:
	"""[summary]
	
	CONSTANTS OF ARES CLASS
	
	Variables:
		{[constant]} -- [description]
		VERSION {str} -- Version of product
		NAME_PRODUCT {str} -- Name of Product
		SITE_WEB {str} -- Site WEB
		COMPANY {str} -- Company Name Copyright
	"""

	VERSION = '1.0'
	NAME_PRODUCT = 'Ares'
	SITE_WEB = ''
	COMPANY = 'Ares Entretainement'

	aObject = {}

	aLibs = []

	aLogs = []

	bIsAdmin = False

	sTimeZone = ''

	sTime = ''


	def getVersion(self):
		if (CONST_INSTALLED == True):
			return self.VERSION
		else:
			return self.getParam('config.version')
	def getNameProduct(self):
		
		if (CONST_INSTALLED == True):
			return self.NAME_PRODUCT
		else:
			return self.getParam('config.name_product')
	
	def getLink(self):
		
		if (CONST_INSTALLED == True):
			return self.SITE_WEB
		else:
			return self.getParam('config.site_web')

	"""getObject()
		-sClass = Classe de l'objet qui sera cree
		-aParams = Params attribues a la classe
	[description]
	Utilisation d'un codage enregistré dans la liste 
	oObjects permettant d'eviter la repetition 
	de code.
	"""
	def getObject(self,sClass,aParams =[]):
		sHash = md5(sClass + serialize(aParams))
		if (sHash in self.aObject.keys()):
			return self.aObject[sHash]

		if(class_exist(sClass) == False):
			buff = Error('ErrorClassModuleExistence', 'Classe' + sClass + 'N\'existe pas')
		
		ClassMod = __import__('class'+sClass, fromlist=[sClass])
		

		if(aParams != []):
			cmd = sClass+'('
			for i in range(len(aParams)):
				cmd += "\""+aParams[i]+"\""
				if (i != len(aParams)-1):
					cmd+= ','
			cmd += ')'
			cmd = 'ClassMod.'+cmd
			self.aObject[sHash] = eval(cmd)
			return self.aObject[sHash] 
		return

	def getPhrase(self,sPrefix,sLang = ''):
		return self.getObject('Language',[sPrefix, sLang]).sPhrase



		






















