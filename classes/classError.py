"""CLASS ERROR

[ERROR CLASS GERE L'ENSEMBLE DES CONFLITS]
S'OCCUPE DE L'ENVOIE D'UN MESSAGE A L'UTILISATEUR
OU AU DEVELOPPEUR EN CAS D'ERREUR EMERGENTE SELON
SON STADE
[ARES PROJECT]
* @copyright		[ARES ENTRETAINEMENT]
* @author			CHOUBIKI Ismael
* @package 			AresTrain
* @version 			$id: classes/classError.py
*

""" 


"""
CONSTANTS

"""
import sys
import datetime




from constants import *

from core.traderror import *
from core.serialize import *


######################




class Error:


	aErrors = {}

	bDisplay = True

	bSkipError = False


	def display(self,sMsg):
		if (PARAM_CONSOLE_MODE == True):
			print "Error Display: " + sMsg
			
		else:
			pass
			####?--
		return 

	def trigger(self, sMsg, sErrorType):
		lib, exist = error_exist(sErrorType)
		if (exist == False):
			self.set(sMsg, sErrorType)
			try:
				raise Exception(sErrorType)
			except Exception as inst:
				x = inst.args
				print 'ErrType : ', x
		else:
			if(lib == 'standard'):
				self.set(sMsg, sErrorType)
				raise Exception(sErrorType)
			else:
				self.set(sMsg, sErrorType)
				self.display(sMsg)
				try:
					raise Exception(sErrorType, get_error_msg(sErrorType))
				except Exception as inst:
					x, y = inst.args
					print 'ErrType : ', x
					print 'ErrMsg  : ', y
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

			self.log(sFileName, sErrorType, sErrorMsg)
			self.trigger(sErrorMsg,sErrorType)
		else:
			#?-- Template
			pass
	def log(self, sFile, sErrorType, sErrorMsg):

		file = open(sFile , 'a')

		aErrorLog =  {'errorType':sErrorType , 'errorMsg':sErrorMsg}
		sErrorLog = serialize(aErrorLog)

		file.write(sErrorLog)
		file.close()

	def backup(self):
		
		file = open(CONST_PATH_SUB_BACKUP_ERRORS, 'a')
		date = str(datetime.datetime.now())
		for e in self.aErrors.keys():
			file.write(e + " : " + self.aErrors[e] + "\n" + date + "\n")

		file.close()


	def skip():
		return 






