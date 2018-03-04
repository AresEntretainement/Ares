from classes.classLanguage import Language
from classes.classError import Error
from classes.classHash import Hash
from core.serialize import serialize, deserialize

d = Language('hello', 'FR').get()
print(d)

f = Hash()
print(f.md5('durand'))

class Hello:
	def __init__(self):
		print('Hello')
	def printing(self):
		print('Hello')

e = Hello()
s = serialize(e)
print(type(s))
print(s)
k = deserialize(s)
print(type(k))
# aReturnList = []
# 			Query = """ SELECT """
# 			for j in aField:
# 				if(j in Tables[sTable].keys()):
# 					pass
# 				else:
# 					#erro
# 					print("ERROR FIELD OR RETURN NOT IN TABLES COLUMNS")
# 					return
# 			for k in dOption.keys():
# 				if(k in Tables[sTable].keys()):
# 					pass
# 				else:
# 					#erro
# 					print("ERROR FIELD OR RETURN NOT IN TABLES COLUMNS RESEARCH")
# 					return
# 			cursor = self.hMaster.cursor()
# 			preList = str(aField).strip('[')
# 			preList = preList.strip(']')
# 			preList = preList.replace("'", '')
# 			Query += preList 
# 			Query += " FROM {0} ".format(str(sTable))
# 			Query += "WHERE "
# 			for index in dOption.keys():
# 				Query += "{0}={1}  AND ".format(index,str(dOption[index]))

# 			Query = Query[:-4]
# 			print(Query)
			
# 			cursor.execute(Query)

# 			aReturnList = cursor.fetchall()
# 			if aReturnList == []:
# 				print('Empty')
# 				return []
# 			else:
# 				return [list(x) for x in aReturnList]
# 		else:
# 			#Error
# 			print('ERROR TABLE DONT EXISTS')
# 		return 

# cursor.execute("SELECT * FROM info WHERE %s=?" % field, (query,))


###############################
			# Query = Query[:-1] + ")"
			# Query += " VALUES("
			# for d in dField.keys():
			# 	Query += ":"+str(d)+", "
			# Query = Query[:-2] + ")"
			# cursor = self.hMaster.cursor()
			# print(Query)
			
			# cursor.execute(Query, dField)
			# id = cursor.lastrowid
			# print('Dernier id: %d' % id)

######################################
			# for _ in dField.keys():
			# 	Query += " ?,"
			# Query = Query[:-1] + ")"
			# cursor = self.hMaster.cursor()
			# print(Query)
			# aListQuery = []
			# for z in dField.keys():
			# 	aListQuery.append(dField[z])
			# cursor.execute(Query, aListQuery)
			# id = cursor.lastrowid
			# print('Dernier id: %d' % id)