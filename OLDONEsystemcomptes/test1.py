import sqlite3 as sql


dicti = {
    'Pseudo' : 'Clemence',
    'Password' : '3ab61be8c01fcd34dfc45eba023c0461', 
    'Admin' : 0, 
    'Mail' : 'clem@ares.com', 
    'Adress' : '1 Impasse Racassiere', 
    'Town' : 'Mortagne-sur-Sevre', 
    'Poids' : 60, 
    'Taille' : 170, 
    'LevelBoxing' : 'F', 
    'LevelAthletics' : 0
}

db = sql.connect('database/database.db')
def getQuery(sTable, dField):
    Query = """ INSERT INTO """
    Query += str(sTable)+ "("
    for i in dField.keys():
        Query += str(i) + ","
    Query = Query[:-1] + ")"
    Query += " VALUES("
    for d in dField.keys():
      Query += ":"+str(d)+", "
    Query = Query[:-2] + ")"
    print(Query)
    return Query

getQuery('Users', '')

# cursor.execute(Query, dField)
# id = cursor.lastrowid
# print('Dernier id: %d' % id)