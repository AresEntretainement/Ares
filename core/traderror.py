
"""
Cherche dans le ficher core.classes l'ensemble des 
classes et verifie l'existence du parametre
"""	

def error_exist(sError):
	from list.listError import aStandardErrorList,dErrorDictionary
	if (sError in aStandardErrorList):
		return 'standard',True
	elif(sError in dErrorDictionary):
		return 'ares_error', True
	else:
		return '',False
def get_error_msg(sError):
	from list.listError import aStandardErrorList,dErrorDictionary
	if (sError in dErrorDictionary):
		return dErrorDictionary[sError]
	else:
		return ''



