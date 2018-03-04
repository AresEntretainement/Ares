subsUsers = 2
subsTrainings = 1
subsExercicesInstalled = 1


QueryTables = {
		'Users' : ['Users', subsUsers],
		'Trainings' : ['Trainings', subsTrainings],
		'ExercicesInstalled' : ['ExercicesInstalled', subsExercicesInstalled]
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
FieldsExercicesInstalled = {
	'*' : None,
	'Prefix' : str,
	'Autor' : str,
	'Types' : str,
	'FilePreload' : str,
	'PathDoc' : str
}

Tables = {
		str(QueryTables['Users'][0]) : FieldsUsers,
		str(QueryTables['Trainings'][0]) : FieldsTrainings,
		str(QueryTables['ExercicesInstalled'][0]) : FieldsExercicesInstalled
}