
import re

ProgramList = ['TrainingRobotSans']
Levels = ['A','B','C']
class Program():

	def __init__(self, file, level):
		self.FilePath = file
		self.LevelUser = level
		self.File = open(self.FilePath,'r')
		self.__call__()
		return
	def __call__(self):
		self.Variables,self.Questions,self.Buttons,self.Program,self.Dictionnary = self.Program()
		self.UserDefault = self.Default()

		return

	def Program(self):
		file = self.File
		DictionnaryVariables = {}
		DictionnaryQuestions = {}
		DictionnaryButtons = {}
		DictionnaryDict = {}
		FieldExpressionVars = 'V-(.)*'
		FieldExpressionQuestions = 'Q-(.)*'
		FieldExpressionButtons = 'B-(.)*'
		FieldExpressionProgram = 'P-(.)*'
		FieldExpressionDict = 'D-(.)*'
		for line in file:
			if (re.search(FieldExpressionVars, line) is not None):
				Field = re.search(FieldExpressionVars, line).group(0).strip('\n').split(':')
				DictionnaryVariables[Field[0]] = Field[1]

			elif (re.search(FieldExpressionQuestions, line) is not None):
				Field = re.search(FieldExpressionQuestions, line).group(0).strip('\n').strip('Q-').split(',')
				DictionnaryQuestions[Field[0]] = {'maxValue' : Field[1].strip('max='),'None' : Field[2]}

			elif (re.search(FieldExpressionButtons, line) is not None):
				Field = re.search(FieldExpressionButtons, line).group(0).strip('\n').strip('B-').split(';')
				DictionnaryButtons[Field[0]] = Field[1]

			elif (re.search(FieldExpressionProgram, line) is not None):
				Program = re.search(FieldExpressionProgram, line).group(0).strip('\n').strip('P-')
				if(Program not in ProgramList):
					raise Exception

			elif (re.search(FieldExpressionDict, line) is not None):
				Field = re.search(FieldExpressionDict, line).group(0).strip('\n').strip('D-').strip('}').split('=')
				Field[1] = Field[1].strip('{')
				Phase = Field[1].split(',')

				TemporalDict = {}
				for element in Phase:
					e = element.split(':')
					TemporalDict[e[0]] = e[1]
				DictionnaryDict[Field[0]] = TemporalDict
			else:
				pass
		return DictionnaryVariables,DictionnaryQuestions,DictionnaryButtons,Program,DictionnaryDict


	def Default(self):
		UserDefault = {}
		if self.LevelUser in Levels:
			for key in self.Dictionnary.keys():
				UserDefault[key] = self.Dictionnary[key][self.LevelUser]
		else:
			raise Exception
		return UserDefault

	def get(self, Var):
		if(Var in self.Variables):
			return self.Variables[Var]
		else:
			return None



test = Program('ShadowBoxing.aee','A')
print test.Program
print test.Dictionnary
print test.UserDefault
