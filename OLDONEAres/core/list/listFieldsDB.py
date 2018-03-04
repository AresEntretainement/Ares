subsUsers = 2
subsTrainings = 1



QueryTables = {
		'Users' : ['Users', subsUsers],
		'Trainings' : ['Trainings', subsTrainings]
}


FieldsUsers = {
	'*' : None,
	'ID' : int,
	'Pseudo' : str,
	'Password' : str,
	'Admin' : int,
	'Mail' : str,
	'Adress' : str,
	'Town' : str,
	'Poids' : int,
	'Taille' : int,
	'LevelBoxing' : str,
	'LevelAthletics' : int
}
FieldsTrainings = {
	'*' : None,
	'ID' : int,
	'Training' : bytes,
	'DateNow' : str,
	'GeneralPerfs' : str
}

Tables = {
		str(QueryTables['Users'][0]) : FieldsUsers,
		str(QueryTables['Trainings'][0]) : FieldsTrainings
}