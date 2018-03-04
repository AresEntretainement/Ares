###CLASS LANGUAGE
# LA CLASSE LANGUAGE CONTRIBUE A LA CREATION
# DE L'OBJET LANGUAGE INVOQUE PAR LA METHODE 
# getPhrase(sPhrase)
# le but est de retourner une traduction convenable
# aux parametres defini par l'utilisateur dans la base 
# de donnes ou ceux qui sont par defaut

# * @copyright		[ARES ENTRETAINEMENT]
# * @author			CHOUBIKI Ismael	
# * @package 		AresTrain
# * @version 		$Id: classes/classLanguage.py


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import os
import importlib
from classes.classError import Error
from classes.classHash import Hash

"""
CONSTANTS

"""



from constants import *

class Language: 

	sLangDefault = ''

	aLangsInstalled = []

	sLangUsed = ''

	sPhrase = ''

	def __init__(self, sPhrase, sLang = ''):
		#Etape recuperation de l'ensemble des languages
		langFiles = self.InstalledLanguages()
		if ('00' in langFiles):
			file = importlib.import_module("lang00")
			codage = file.codage
			langFiles.remove('00')
			files = ['lang' + x for x in langFiles]
			Codages = {}
			for i in files:
				file = importlib.import_module(i)
				Codages[i[4:6]] = file.codage
				del(file)
			sVersion = codage[73:]
			for i in Codages.keys():
				code = Hash()
				if (code.getCodecVersion(i,'Language',Codages[i],sVersion)):
					self.aLangsInstalled.append(i)
				else: 
					langFiles.remove(i)
			if (PARAM_DEV_MODE == False):
				#?--Database
				pass
			else:
				if( self.IsPhrase(sPhrase)):
					if (sLang != ''):
						if(sLang in self.aLangsInstalled):
							file = importlib.import_module('lang' + sLang)
							if (sPhrase in file.Dictionnary):
								self.sPhrase = file.Dictionnary[sPhrase]
							else:
								error = Error()
								error.errorHandler('ErrorLangPhraseExistencePackage', 'Phrase dont exist in this package Language')
						else:
							error = Error()
							error.errorHandler('ErrorLangExistence', 'Language not installed')
					elif (PARAM_LANG_DEFAULT in self.aLangsInstalled):
						self.sLangDefault = PARAM_LANG_DEFAULT
						self.sLangUsed = PARAM_LANG_DEFAULT
						if(sPhrase in self.getLangBy(self.sLangUsed)):
							file = importlib.import_module('lang' + self.sLangUsed)
							self.sPhrase = file.Dictionnary[sPhrase]
						else:
							error = Error()
							error.errorHandler('ErrorLangPhraseExistencePackage', 'Phrase dont exist in this package Language')
					else:
						error = Error()
						error.errorHandler('ErrorInstallLang', 'Default Language Not Installed!')			
				else:
					error = Error()
					error.errorHandler('ErrorLangPhraseExistenceDictionnary', 'Phrase dont exist in this package Language')

		else: 
			error = Error()
			error.errorHandler('ErrorInstallLang', 'Language Initialization Object')


	def InstalledLanguages(self):
		path = os.getcwd().replace(CONST_ARES_CLASSES,'') + CONST_ARES_SEPARATOR + CONST_ARES_LANG + CONST_ARES_SEPARATOR
		sys.path.append(path)
		listFiles = os.listdir(path)
		if ('__pycache__' in listFiles):
			listFiles.remove('__pycache__')
		langFiles = list(set([x[4:6] for x in listFiles]))


		return langFiles
	def IsPhrase(self, sPhrase):
		from lang.lang00 import DictionnaryItems
		if(sPhrase in DictionnaryItems):
			return True
		else:
			return False

	def getLangBy(self, sVar):
		if (sVar in self.aLangsInstalled):
			file = importlib.import_module('lang'+sVar)
			return file.Dictionnary 
		else:
			error = Error()
			error.errorHandler('ErrorInstallLang', 'Language Not Installed')
	def get(self):
		return self.sPhrase
