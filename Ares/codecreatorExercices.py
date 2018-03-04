from controllers.controllerDB import ControllerDB

d = ControllerDB()

# Query = """
# CREATE TABLE  IF NOT EXISTS ExercicesInstalled(
# 	Prefix TEXT,
# 	Autor TEXT,
# 	Types TEXT,
# 	FilePreload TEXT,
# 	PathDoc TEXT
# )"""
# dicti = {
# 	'Prefix' : 'Burpee',
# 	'Autor' : 'Ares Entretainements',
# 	'Types' : '[ExerciceCardioVascular,ExerciceMuscular]',
# 	'FilePreload' : 'Burpees.aee',
# 	'PathDoc' : 'modules.Training.Burpees'
# }

if 'Burpees' in d.getExercicesInstalled():

# : ExerciceMuscular
# : ExerciceCardioVascular
# : ExerciceWithStrike
# : RobotTrainSparbar
# : RobotTrain
# : ExerciceStart

Burpees = {
	'Prefix' : 'Burpee',
	'Autor' : 'Ares Entretainements',
	'Types' : '[ExerciceCardioVascular,ExerciceMuscular]',
	'FilePreload' : 'Burpees.aee',
	'PathDoc' : 'modules.Training.Burpees'
}
CordeSauter = {
	'Prefix' : 'CordeSauter',
	'Autor' : 'Ares Entretainements',
	'Types' : '[ExerciceCardioVascular]',
	'FilePreload' : 'CordeSauter.aee',
	'PathDoc' : 'modules.Training.CordeSauter'
}
Pao = {
	'Prefix' : 'Pao',
	'Autor' : 'Ares Entretainements',
	'Types' : '[RobotTrain]',
	'FilePreload' : 'Pao.aee',
	'PathDoc' : 'modules.Training.Pao'
}
Pompes = {
	'Prefix' : 'Pompes',
	'Autor' : 'Ares Entretainements',
	'Types' : '[ExerciceMuscular]',
	'FilePreload' : 'Pompes.aee',
	'PathDoc' : 'modules.Training.Pompes'
}
ShadowBoxing = {
	'Prefix' : 'ShadowBoxing',
	'Autor' : 'Ares Entretainements',
	'Types' : '[ExerciceStart]',
	'FilePreload' : 'ShadowBoxing.aee',
	'PathDoc' : 'modules.Training.ShadowBoxing'
}
Sparring = {
	'Prefix' : 'Sparring',
	'Autor' : 'Ares Entretainements',
	'Types' : '[RobotTrainSparbar]',
	'FilePreload' : 'Sparring.aee',
	'PathDoc' : 'modules.Training.Sparring'
}
Squat = {
	'Prefix' : 'Squat',
	'Autor' : 'Ares Entretainements',
	'Types' : '[ExerciceMuscular]',
	'FilePreload' : 'Squat.aee',
	'PathDoc' : 'modules.Training.'
}
TechnicalPower = {
	'Prefix' : 'TechnicalPower',
	'Autor' : 'Ares Entretainements',
	'Types' : '[ExerciceWithStrike]',
	'FilePreload' : 'TechnicalPower.aee',
	'PathDoc' : 'modules.Training.TechnicalPower'
}
TechnicalVelocity = {
	'Prefix' : 'TechnicalVelocity',
	'Autor' : 'Ares Entretainements',
	'Types' : '[ExerciceWithStrike]',
	'FilePreload' : 'TechnicalVelocity.aee',
	'PathDoc' : 'modules.Training.TechnicalVelocity'
}
ModulesInstalled = {
	'TechnicalVelocity': TechnicalVelocity,
	'TechnicalPower':TechnicalPower,
	'Squat' : Squat,
	'Sparring' : Sparring,
	'ShadowBoxing' : ShadowBoxing,
	'Pompes' : Pompes,
	'CordeSauter' : CordeSauter,
	'Burpees' : Burpees,
	'Pao' : Pao
}

# for i in ModulesInstalled.keys():
# 	d.installExercice(ModulesInstalled[i])