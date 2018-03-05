
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

"""
Cherche dans le ficher core.classes l'ensemble des 
classes et verifie l'existence du parametre
"""	

def error_exist(sError):
	from core.list.listError import aStandardErrorList,dErrorDictionary
	if (isinstance(sError, str)):
		if (sError in aStandardErrorList):
			return 'standard',True
		elif(sError in dErrorDictionary):
			return 'ares_error', True
		else:
			return '',False
	else: 
		if (sError.__name__ in aStandardErrorList):
			return 'standard',True
		elif(sError.__name__ in dErrorDictionary):
			return 'ares_error', True
		else:
			return '',False
def get_error_msg(sError):
	from core.list.listError import aStandardErrorList,dErrorDictionary
	if (sError in dErrorDictionary):
		return dErrorDictionary[sError]
	else:
		return ''



