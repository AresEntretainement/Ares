# CLASS ERROR

# [ERROR CLASS GERE L'ENSEMBLE DES CONFLITS]
# S'OCCUPE DE L'ENVOIE D'UN MESSAGE A L'UTILISATEUR
# OU AU DEVELOPPEUR EN CAS D'ERREUR EMERGENTE SELON
# SON STADE
# [ARES PROJECT]
# * @copyright		[ARES ENTRETAINEMENT]
# * @author			CHOUBIKI Ismael
# * @package 			AresTrain
# * @version 			$id: classes/classError.py



from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import sys
import datetime
import traceback



from constants import CONST_PATH_SUB_ERRORLOG, CONST_PATH_SUB_BACKUP_ERRORS, PARAM_CONSOLE_MODE

from core.traderror import *
from core.serialize import *


######################



class Error:


	aErrors = {}

	bDisplay = True

	bSkipError = False

	def __init__(self, sErrorType, sErrorMsg, bSkip = False, aVars = [], sFileName = CONST_PATH_SUB_ERRORLOG):
		if (bSkip):
			self.skip()
		self.errorHandler(sErrorType, sErrorMsg, sFileName, aVars)

	def display(self,errorType,sMsg, sType = ''):
		if (PARAM_CONSOLE_MODE == True):
			msg = "\nError Display : {0}Error Message : {1}\nError Type : {2}".format(traceback.format_exc(), sMsg,[errorType.__name__, sType])
			raise errorType(msg)
		else:
			pass
			####?--
		return 

	def trigger(self, sErrorType, sMsg, sFile = ''):
		lib, exist = error_exist(sErrorType)
		if (exist == False):
			self.set(sMsg, sErrorType)
			try:
				raise Exception(sErrorType)
			except Exception as inst:
				x = inst.args
				print('ErrType : ', x)
		else:
			if(lib == 'standard'):
				self.set(sMsg, sErrorType)
				self.log(sFile, sErrorType.__name__, sMsg)
				self.display(sErrorType, sMsg)
			elif (lib == 'ares_error'):
				self.set(sMsg, sErrorType)
				try:
					self.log(sFile,sErrorType, sMsg)
					self.display(TypeError, get_error_msg(sErrorType), sErrorType)

				except Exception as inst:
					x= inst.args
					string =  str(x[0]) 
					print(string)
			else:
				raise Exception
		return


	def set(self, sMsg, sErrorType):
		i = 2
		while (sMsg in self.aErrors):
			if (i==2):
				sMsg = sMsg + str(i)
			else:
				sMsg = sMsg[:-1] + str(i)
			i = i + 1
		self.aErrors[sMsg] = sErrorType

		return False

	def get(self):
		return self.aErrors

	def setDisplay(b_Display):
		self.bDisplay = b_Display

	def getDisplay(self):
		return self.bDisplay

	def whatIsPassed(self):
		return len(self.aErrors)
	def reset(self):
		self.aErrors = {}

	def errorHandler(self, sErrorType, sErrorMsg, sFileName = CONST_PATH_SUB_ERRORLOG, aVars = []):
		if (self.bSkipError):
			return False

		if (PARAM_CONSOLE_MODE):
			self.trigger(sErrorType, sErrorMsg, sFileName)
		else:
			#?-- Template
			pass
	def log(self, sFile, sErrorType, sErrorMsg ):
		with open(sFile, 'a') as file:
			aErrorLog =  {'errorType':str(sErrorType) , 'errorMsg':str(sErrorMsg)}
			sErrorLog = str(serialize(aErrorLog))
			file.write(sErrorLog)
		return 

	def backup(self):
		with open(CONST_PATH_SUB_BACKUP_ERRORS, 'a') as file:
			date = str(datetime.datetime.now())
			for e in self.aErrors.keys():
				file.write(e + " : " + self.aErrors[e] + " -- " + date + "\n")
	def skip(self):
		self.bSkipError = True
		return 






