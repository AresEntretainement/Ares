
# DB = Database()
# DB.connect()
# #print(DB.selector('Users',['*'],1))
# #DB.update('Users', {'Pseudo' : 'Clemenceeu'}, {'Town' : "'Mortagne-sur-Sevre'"})
# encode = DB.search('Users',['*'],{'Poids' : 80})
# print(encode)
dicti = {
    'Pseudo' : 'Clemenc',
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

# #DB.delete('Users', {'Poids' : 60} )
# e = Hash()
# a = '4284c31bf5f153a29a87fa16f6a2b538851865181c026e4b9993db83d3ee2c82b8c91e0111'
# b = 'a730d90cda9087e96349ed94828d4bedd286150e7fb941bb026fad69be7233775ad0765ef9'

# d.DB.update('Users', {'Password' : b} , {'Pseudo' : "'AresUser'"})
# print(d.DB.search('Users',['*'], {'Pseudo' : 'AresUser'}))
d = ControllerDB()
#d.DB.delete('Users',{'Pseudo' : 'Clemenc'})
#print(d.DB.query(""" SELECT * FROM Users """))
# print(d.DB.query(""" SELECT Pseudo FROM Users"""))
#d.createUser(dicti)
#d.deleteUser('Clemenc')
#d.changeFieldsUser('Clemence',dicti)
#print(d.getFieldUser('AresUser','Town'))
#print(d.getID('AresUser'))
#print(d.searchTrainigsUser('AresUser'))
# alpha = pickle.dumps(dicti)
# other = {
#     'Training' :  alpha,
#     'DateNow' : '1-03-2018',
#     'GeneralPerfs' : '[]'
# }
#d.registreTraining('AresUser',other)
#print(d.DB.query(""" SELECT * FROM Trainings"""))
# e = d.searchTrainigsUser('AresUser')
# e = e[1][1]
# beta = pickle.loads(e)
# print(beta)