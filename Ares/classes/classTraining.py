EvaluationTraining = { 1 : 'ShadowBoxing', 2 : 'CordeSauter', 3 : 'Pompes' , 4 : 'Squat' , 5 : 'Burpees', 6 : 'TechnicalPower' , 7 : 'TechnicalVelocity' , 8 : 'Pao' , 9 : 'Sparring'}
"""
TEST
"""


#Constantes Parametriques:
from constants import CONST_EXTENSION, CONST_PATH_TRAINING


#BASE DE DONNES A REMPLACER:

#Type d'entrainement installé
ProgramList = ['ExerciceWithStrike','RobotTrainSparbar','RobotTrain','ExerciceMuscular','ExerciceCardioVascular','ExerciceStart']

#Niveaux Installes 
Levels = ['A','B','C']

#Implementation des modules et librairies Python
import re
import asyncio
import os

#Implementation des differents Composants
from modules.Training.chargeModules import ModulesInstalled 
import classes.classProgram as Program

class Train:
    def __init__(self,Training,EvaluationMode = False):
        self._Training = Training
        self.TrainingParties = self.loadTrains(Training)
    def loadTrains(self,Training):

        ReturnLoadedTrains = {}
        for exercice in Training.values():
            if (exercice not in ModulesInstalled):
                #Remplace par module Error : Modules in Train Not installed
                print("Error : MODULE IN TRAINING NOT INSTALLED")
            for key, value in self._Training.items():   
                if value == exercice:
                    lKey = key
                    ReturnLoadedTrains[lKey] = Program.Program((CONST_PATH_TRAINING + exercice + CONST_EXTENSION))
        return ReturnLoadedTrains



