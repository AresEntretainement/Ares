"""
Classe Capable de lire l'ensemble des programmes installées
Categorie de Programmes
: ExerciceMuscular
: ExerciceCardioVascular
: ExerciceWithStrike
: RobotTrainSparbar
: RobotTrain

"""


CONST_TRAINING = "Training"

import re
import importlib
from controllerRobot import controllerRobot 
TypesList = ['ExerciceCardioVascular','ExerciceMuscular','ExerciceStart','RobotTrain','RobotTrainSparbar','ExerciceWithStrike']

class Program():
    

    def __init__(self, file = ''):

        #Selection of file Path
        self.FilePath = file

        #Get SETTINGS of Program
        self.GeneralSetting = self.Settings()

        #Import Controller
        self.Controller = self.ImportController()

        #Get CONTROLLER TYPE of Program in ElementController
        self.Type = self.Controller.Type

        self.ElementController = self.ImportElementController()




    def ImportElementController(self):
        if (isinstance(self.Type, list)):
            Temporal = {}
            for element in self.Type:
                if(element in TypesList):
                    Temporal[element] = exec("self.controller" + element + "()")
                else:
                    #Remplace Module Error
                    print('Error: CONTROLLER ELEMENT NOT EXISTANT')
                #Query = "self.ElementController['"+element+"'] = self.controller" + element + "()"
                #exec(Query)
            return Temporal
        else:
            if(self.Type in TypesList):
                print('HERE')
                if (self.Type == 'ExerciceCardioVascular'):
                    return self.controllerExerciceCardioVascular()
                else:
                    Temporal = exec("self.controller"+element+"()")
                    return Temporal
            else:
                #Remplace Module Error
                print('Error : TYPE CONTROLLER DONT EXISTANT')



    def controllerRobotTrain(self): 
        return

    def controllerRobotTrainSparbar(self): 
        robot = controllerRobot.ControllerRobot('Main')
        return robot

    def controllerExerciceWithStrike(self): 
        return

    def controllerExerciceCardioVascular(self): 
        #Testing a remplacer
        robot = controllerRobot.ControllerRobot('Main')
        print('INCONTROLLER')
        return robot

    def controllerExerciceMuscular(self): 
        #testing a remplacer
        robot = controllerRobot.ControllerRobot('Main')
        return robot

    def controllerExerciceStart(self): 
        return 


    #METHOD FOR GET SETTINGS OF PROGRAM

    def Settings(self,sFile = ''):

        if(sFile == ''):
            sFile = self.FilePath

        ObjectsRegex = re.compile('Objects ?= ?/(.+?)/')
        file = open(sFile,'r').read()
        MatchesObjects = ObjectsRegex.match(file).groups(0)[0].split(',')
        FieldsRegex = MatchesObjects[-1][7:]

        if(FieldsRegex == 'Empty'):
            FieldsRegex = []
        else:
            FieldsRegex = FieldsRegex.split(';')

        MatchesObjects.pop(-1)
        DictRegex = {}
        ReturnReg = {}
        ReturnReg['Field'] = {}

        for match in MatchesObjects + FieldsRegex:
            DictRegex[match] = re.compile(r"<" + match + ">(.+?)<End" + match + ">")

        for Object in DictRegex.keys():
            if(DictRegex[Object].search(file) == None):
                #Remplace par Module erreur
                print(Object + 'Error : COMPONNENT DONT EXIST IN FILE')

            else:

                if(Object in FieldsRegex):
                    DictRegex[Object]= DictRegex[Object].search(file).groups(0)[0].strip().split(';')
                    ReturnReg['Field'][Object] = {}

                    for Caracteristique in DictRegex[Object]:
                        temporalVar = Caracteristique.split('=')
                        if(',' in temporalVar[1]):
                            Raw = temporalVar[1].strip().split(',')
                            ReturnReg['Field'][Object][temporalVar[0].strip()] =  {}

                            for index in range(len(Raw)):
                                if ('/' in Raw[index]):
                                    temporalString =  Raw[index].split('/')
                                    ReturnReg['Field'][Object][temporalVar[0].strip()][temporalString[0]] = temporalString[1]
                                else:
                                    #Remplace Error Non ASIGNEMENT IN SET FILE
                                    print("Error : NOT ASSIGNEMENT IN SET FILE")

                        else:
                            ReturnReg['Field'][Object][temporalVar[0].strip()] = temporalVar[1].strip()
                else:
                    DictRegex[Object]= DictRegex[Object].search(file).groups(0)[0].strip().split(';')
                    ReturnReg[Object] = {}

                    for Caracteristique in DictRegex[Object]:
                        temporalVar = Caracteristique.split('=')
                        if(',' in temporalVar[1]):
                            ReturnReg[Object][temporalVar[0].strip()] = temporalVar[1].strip().split(',')

                        else:
                            ReturnReg[Object][temporalVar[0].strip()] = temporalVar[1].strip()

        if(ReturnReg['Field'] == {}):
            del(ReturnReg['Field'])
        ####CHARGE SETTINGS####
        
        return ReturnReg

    def ImportController(self):
        imported = importlib.import_module(CONST_TRAINING + '.' + self.GeneralSetting['Proprieties']['Prefix'] + '.controller' + self.GeneralSetting['Proprieties']['Prefix'])
        Object = eval('imported.' + self.GeneralSetting['Proprieties']['Prefix'] + "(self.GeneralSetting)")
        if (self.VerificationController(imported, Object)):
            return Object
        else:
            #Remplace for module ERROR : Module PACKAGE PROPRIETIES NOT INSTALLED
            print('Error : PACKAGE PROPRIETIES NOT INSTALLED')
            assert Exception

    def VerificationController(self,mModule, oObject):
        INSTALLPACK = mModule.INSTALL_PACKAGE_INFOS
        for key in oObject.Doc.keys():
            if (key == 'Field'):
                for newKey in oObject.Doc['Field'].keys():
                    if(newKey not in INSTALLPACK):
                        #Remplace For Module Error 
                        print('Error : SETTING NOT IN INSTALLPACK')
                        return False
            if(key not in INSTALLPACK):
                print(key)
                #Remplace For Module Error KEY DONT EXIST IN PACKAGE
                print('Error : KEY SETTINGS DONT EXIST IN PACKAGE')
                return False
        return True 

    def Default(self):
        UserDefault = {}
        if self.LevelUser in self.Levels:
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


