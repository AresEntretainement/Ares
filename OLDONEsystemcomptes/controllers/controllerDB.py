from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from classes.classHash import Hash
from classes.classDatabase import Database as DB
from core.list.listFieldsDB import QueryTables, Tables


class ControllerDB:
	DB = None
	def __init__(self):
		self.Hash = Hash()
		self.DB = DB()
		self.DB.connect()
		return
	def verifyDictionnary(self, dFields, bAll = True, sTable = QueryTables['Users'][0]):
		if (bAll):
			if (sTable in Tables.keys()):
				LenFieldUsers = len(Tables[sTable]) - QueryTables[sTable][1]
				if(len(dFields.keys()) == LenFieldUsers):
					for field in dFields.keys():
						if (field in Tables[sTable].keys()):
							if (isinstance(dFields[field], Tables[sTable][field])):
								pass
							else:
								#Error
								print('ERROR FIELDS NOT CORRECT TYPE VALUE')
								return False
						else:
							#Error
							print('ERROR FIELDS NOT CORRECT ID DICTIONNARY')
							return False
					return True
				else:
					#Error
					print('ERROR NOT ALL FIELDS FOR CREATE USER')
					return False
			else:
				#error
				print('ERROR TABLE DONT EXISTS')
				return False
		else:
			for field in dFields.keys():
				if (field in Tables[sTable].keys()):
					if (isinstance(dFields[field], Tables[sTable][field])):
						pass
					else:
						#Error
						print('ERROR FIELDS NOT CORRECT TYPE VALUE')
						return False
				else:
					#Error
					print('ERROR FIELDS NOT CORRECT ID DICTIONNARY USER')
					return False
			return True
	def isField(self, sField, sTable = 'Users'):
		if (sField in Tables[QueryTables[sTable][0]].keys()):
			return True
		else:
			return False
	def getID(self, sField, sDataset = 'Pseudo'):
		if (sDataset == 'Pseudo'):
			return self.DB.search(QueryTables['Users'][0], ['ID'], {'Pseudo' : sField})[0][0]
		else:
			if (self.isField(sDataset)):
				return sum(self.DB.search(QueryTables['Users'][0], ['ID'], {sDataset : sField}), [])
			else:
				#error
				print("ERROR IS NOT FIELD")
	def userExists(self, sUser):
		return self.DB.exists(QueryTables['Users'][0], 'Pseudo', sUser)

	def verifyPass(self, sUser, sPassword):
		if(self.userExists(sUser)):
			Password = self.DB.search(QueryTables['Users'][0], ['Password'], {'Pseudo' : str(sUser)})[0][0]
			return self.Hash.comparePassHash(sPassword, Password)
		else:
			return False
	def createUser(self, dFields):
		if (self.verifyDictionnary(dFields)):
			if (self.userExists(dFields['Pseudo'])):
				#Error
				print('ERROR USER ALREADY EXIST USE AN OTHER PSEUDO')
				return 
			else:
				dFields['Password'] = str(self.Hash.getPassHash(dFields['Password']))
				self.DB.insert(QueryTables['Users'][0], dFields)
				print('USER CREATED!')
				
		else:
			return
	def deleteUser(self, sUser):
		if(self.DB.exists(QueryTables['Users'][0], 'Pseudo', sUser)):
			self.DB.delete(QueryTables['Users'][0], {'Pseudo' : sUser})
		else:
			#error
			print('ERROR USER DOESNT EXISTS')
		return
	def changeFieldsUser(self, sUser, dField):
		if(self.userExists(sUser)):
			if (self.verifyDictionnary(dField, False)):
				self.DB.update(QueryTables['Users'][0], dField, {'Pseudo' : sUser})
			else:
				return
		else:
			#error
			print('ERROR USER DOESNT EXIST')
			return
	def getFieldUser(self, sUser, sField):
		if (self.userExists(sUser)):
			if (self.isField(sField)):
				return sum(self.DB.search(QueryTables['Users'][0], [sField] , {'Pseudo' : sUser}),[])
			else:
				#error
				print('ERROR FIELD DONT EXISTS')
				return
		else:
			#error
			print('ERROR USER DONT EXISTS')
			return
	def searchTrainigsUser(self, sUser):
		if (self.userExists(sUser)):
			ID = self.getID(sUser)
			if (self.DB.exists(QueryTables['Trainings'][0], 'ID', ID)):
				return self.DB.search(QueryTables['Trainings'][0], ['*'], {'ID' : ID})
			else:
				#error
				print("ERROR USER DONT'T HAVE TRAININGS DOIT")
				return 
		else:
			#error
			print('ERROR USER DONT EXISTS')
			return
	def registreTraining(self, sUser, dFields):
		dFields['ID'] = 1
		if (self.verifyDictionnary(dFields, True, QueryTables['Trainings'][0])):
			if(self.userExists(sUser)):
				ID = self.getID(sUser)
				dFields['ID'] = int(ID)
				self.DB.insert(QueryTables['Trainings'][0], dFields)
				print('Training Inserted')
			else:
				print("ERROR USER DONT EXISTS")
		else:
			return
