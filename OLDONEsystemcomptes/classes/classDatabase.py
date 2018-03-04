from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sqlite3 as sql
from constants import ARES_SETTINGS_DATABASE_PATH, ARES_SETTINGS_DATABASE_NAME
from core.list.listFieldsDB import Tables, FieldsUsers, FieldsTrainings




class Database:

	hMaster = None
	hSlave = None
	sIsSlave = ''

	def connect(self, sDatabase = ARES_SETTINGS_DATABASE_NAME, sPath = ARES_SETTINGS_DATABASE_PATH):
		if (sPath):
			if (sDatabase):
				sHost = sPath + sDatabase
				try:
					self.hMaster = sql.connect(sHost)
				except:
					#Error
					print("ERROR CONNEXTION TO DATABASE, PATH AND DATABASE NOT IDEAL")
			else:
				sHost = sPath + sDatabase
				try:
					self.hMaster = sql.connect(sHost)
				except:
					#Error
					print("ERROR CONNEXION TO DATABASE, PATH NOT IDEAL")
		else:
			sHost = sPath + sDatabase
			try:
				self.hMaster = sql.connect(sHost)
			except:
				#Error
				print("ERROR CONNEXION TO DATABASE")
		return True

	def getVersion():
		return str(sql.version)

	def getDatabaseInfo():
		return 'SQLite ' + self.getVersion() 

	def query(self, sSql,aParams = []):
		cursor = self.hMaster.cursor()
		cursor.execute(sSql, aParams)
		results = cursor.fetchall()

		if results:
			return results
		else:
			#error
			print("ERROR QUERY DONT HAVE MATCHES")
	def executeCode(self, sSql, aParams = []):
		if (sSql.count('?') > 0 and sSql.count('?') == len(aParams)):
			cursor = self.hMaster.cursor()
			cursor.execute(sSql, aParams)
			self.hMaster.commit()
		elif (sSql.count('?') == len(aParams)):
			cursor = self.hMaster.cursor()
			cursor.execute(sSql)
			self.hMaster.commit()
		else:
			#error
			print("ERROR PARAMS NOT GOOD")
	def selector(self, sTable, aField, bAll = False ,iNumberR = 1):
		if (sTable in Tables.keys()):
			aReturnList = []
			Query = """ SELECT """
			for j in aField:
				if(j in Tables[sTable].keys()):
					pass
				else:
					#erro
					print("ERROR FIELD OR RETURN NOT IN TABLES COLUMNS ")
					return
			cursor = self.hMaster.cursor()
			preList = str(aField).strip('[')
			preList = preList.strip(']')
			preList = preList.replace("'", '')
			Query += preList
			Query += " FROM {0} ".format(str(sTable))
			cursor.execute(Query)
			if (bAll == True):
				aReturnList = cursor.fetchall()
			else:
				for _ in range(iNumberR):
					try:
						aReturnList.append(cursor.fetchone())
					except:
						#error
						print("PAS ASSEZ DE VALEURS A RETOURNER")
						pass
			return [list(x) for x in aReturnList]
		else:
			#Error
			print('ERROR TABLE DONT EXISTS')
	def search(self, sTable, aField, dOption = {'ID' : 1 }):
		if (sTable in Tables.keys()):
			aReturnList = []
			aListExecute = []
			Query = """ SELECT """
			for j in aField:
				if(j in Tables[sTable].keys()):
					pass
				else:
					#erro
					print("ERROR FIELD OR RETURN NOT IN TABLES COLUMNS")
					return
			for k in dOption.keys():
				if(k in Tables[sTable].keys()):
					pass
				else:
					#erro
					print("ERROR FIELD OR RETURN NOT IN TABLES COLUMNS RESEARCH")
					return
			cursor = self.hMaster.cursor()
			preList = str(aField).strip('[')
			preList = preList.strip(']')
			preList = preList.replace("'", '')
			Query += preList 
			Query += " FROM {0} ".format(str(sTable))
			Query += "WHERE "
			for index in dOption.keys():
				Query += "{0} = (?)  AND ".format(index)
				aListExecute.append(str(dOption[index]))

			Query = Query[:-4]		
			cursor.execute(Query, aListExecute)

			aReturnList = cursor.fetchall()
			if aReturnList == []:
				return []
			else:
				return [list(x) for x in aReturnList]
		else:
			#Error
			print('ERROR TABLE DONT EXISTS')
		return 

	def insert(self, sTable, dField):
		if (sTable in Tables.keys()):
			aReturnList = []
			aListExecute = []
			Query = """ INSERT INTO """
			Query += str(sTable)+ "("
			for j in dField.keys():
				if(j in Tables[sTable].keys()):
					pass
				else:
					#error
					print("ERROR FIELD OR RETURN NOT IN TABLES COLUMNS")
					return
			for i in dField.keys():
				if (isinstance(dField[i], Tables[sTable][i])):
					Query += str(i) + ","
				else:
					#error
					print('ERROR FIELD INSERT NOT CORRESPOND TO TYPE DATA')
					return
			Query = Query[:-1] + ")"
			Query += " VALUES("
			for d in dField.keys():
				Query += ":"+str(d)+", "
			Query = Query[:-2] + ")"
			cursor = self.hMaster.cursor()
			cursor.execute(Query, dField)
			self.hMaster.commit()
		else:
			#Error
			print('ERROR TABLE DONT EXISTS')
		return

	def roll(self):
		self.hMaster.rollback()

	def update(self, sTable, dField, dOption = {'ID' : 1 }):
		if (sTable in Tables.keys()):
			aListExecute = []
			Query = """ UPDATE """
			Query += str(sTable)
			Query += " SET "
			for j in dField.keys():
				if(j in Tables[sTable].keys()):
					Query += str(j) + " = ?, "
					aListExecute.append(dField[j])
				else:
					#erro
					print("ERROR FIELD OR RETURN NOT IN TABLES COLUMNS")
					return
			Query = Query[:-2]
			Query += " WHERE "
			for k in dOption.keys():
				if(k in Tables[sTable].keys()):
					Query += str(k) + " = '" + str(dOption[k]) + "' AND "
				else:
					#erro
					print("ERROR FIELD OR RETURN NOT IN TABLES COLUMNS RESEARCH")
					return
			Query = Query[:-4]
			cursor = self.hMaster.cursor()
			
			cursor.execute(Query, aListExecute)
			self.hMaster.commit()
			print('UPDATED!')
		else:
			#Error
			print('ERROR TABLE DONT EXISTS')
		return 

	def delete(self, sTable, dOption = {'ID' : 1 }):
		if (sTable in Tables.keys()):
			aReturnList = []
			aListExecute = []
			Query = """ DELETE FROM """
			Query += str(sTable)
			Query += " WHERE "
			for k in dOption.keys():
				if(k in Tables[sTable].keys()):
					Query += str(k) + " = :" + str(k) + " AND "
				else:
					#erro
					print("ERROR FIELD OR RETURN NOT IN TABLES COLUMNS RESEARCH")
					return
			Query = Query[:-4]
			cursor = self.hMaster.cursor()
			cursor.execute(Query, dOption)
			self.hMaster.commit()
			print("DELETED")
		else:
			#Error
			print('ERROR TABLE DONT EXISTS')
		return 

	def delByID(self, sTable, iID):
		if (sTable in Tables.keys()):
			self.delete(sTable, {'ID' : iID})
		else:
			#Error
			print('ERROR TABLE DONT EXISTS')
	def getByID(self, sTable, iID):
		if (sTable in Tables.keys()):
			return self.search(sTable, ['*'], {'ID' : iID})
		else:
			#error
			print('ERROR TABLE DONT EXISTS')
	def exists(self, sTable, sField, sCompare):
		if (sTable in Tables.keys()):
			if (sField in Tables[sTable].keys()):
				if (self.search(sTable, [sField], { sField : sCompare}) == []):
					return False
				else:
					return True
			else:
				#error 
				print('ERROR FIELD DONT EXISTS IN TABLE')
				return
		else:
			#error
			print('ERROR TABLE DONT EXISTS')
			return
