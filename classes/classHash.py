# Ares Heades
#
# [Hash Class Codage and Debug]
# 
# -*-coding:utf-8 -*-
#
# [ARES PROJECT]
# * @copyright		[ARES ENTRETAINEMENT]
# * @author			CHOUBIKI Ismael
# * @package 			AresTrain
# * @version 			$id: classes/classHash.py



from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import hashlib
import pickle
import sys

from random import randint


from constants import *




"""CLasse pour creation de codages propres a Ares 
personalises minimisant les chance de brutal force

[Class Hash]
-setHash : Returne une cle de codage propre a l'algorithme 
		   avec un salt personalizable dans les parametres
-setRandomHash : Retourne une cle aleatoire de codage avec un algorithme different
				 Selon les parametres un salt peut etre ajoute ou pas
-getRandomHash : Retourne une valeur bool pour savoir si le decodage est vrai


"""


class Hash:

	def md5(self,sHash):
		return hashlib.md5(str.encode(sHash)).hexdigest()
	def sha1(self,sHash):
		return hashlib.sha1(str.encode(sHash)).hexdigest()
	def sha224(self,sHash):
		return hashlib.sha224(str.encode(sHash)).hexdigest()
	def sha256(self,sHash):
		return hashlib.sha256(str.encode(sHash)).hexdigest()
	def sha384(self,sHash):
		return hashlib.sha384(str.encode(sHash)).hexdigest()
	def sha512(self,sHash):
		return hashlib.sha512(str.encode(sHash)).hexdigest()

	def setHash(self,sPassword, sSalt = ''):
		if (sSalt == ''):
			sSalt = PARAM_SALT
		return self.sha256(md5(sPassword) + self.md5(sSalt))

	def setRandomHash(self, sPassword):
		if (PARAM_CUSTOM_HASH_SALT):
			sPassword = sPassword + PARAM_SALT
		sSeed = ''
		substr = '0123456789abcdef'
		for i in range(0,10):
			randomInt = randint(0, len(substr)-1)
			sSeed += substr[randomInt]
		print(sSeed)
		return self.sha256(sSeed + self.md5(sPassword) + sSeed) + sSeed
	def setCodecVersion(self, sParam, sFirstParam, sVersion):
		sPassword = sParam
		if (PARAM_CUSTOM_HASH_SALT):
			sPassword = sParam + PARAM_SALT
		sSeed = ''
		substr = '0123456789abcdef'
		for i in range(0,10):
			randomInt = randint(0, len(substr)-1)
			sSeed += substr[randomInt]
		return self.sha256(self.sha1(sFirstParam) + self.sha1(sPassword)) + sSeed + sVersion

	def getCodecVersion(self, sParam, sFirstParam, sStoredValue, sVersion):
		sPassword = sParam
		if (PARAM_CUSTOM_HASH_SALT):
			sPassword = sParam + PARAM_SALT

		if (len(sStoredValue) < 64):
			return False
		sStoredSeed = sStoredValue[64 : 74]

		if ((self.sha256(self.sha1(sFirstParam) + self.sha1(sPassword)) + sStoredSeed + sVersion) == sStoredValue):
			return True
		else:
			return False

	def getRandomHash(self, sPassword, sStoredValue):
		if (PARAM_CUSTOM_HASH_SALT):
			sPassword = sPassword + PARAM_SALT
		if (len(sStoredValue) < 64):
			return False
		sStoredSeed = sStoredValue[64 : 74]
		if ((self.sha256(sStoredSeed + self.md5(sPassword) + sStoredSeed) + sStoredSeed) == sStoredValue):
			return True
		else:
			return False
