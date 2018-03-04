"""
Partie du programme qui Enchaine le programme d'entrainement
d'après le niveau obtenu lors de l'evaluation en selectionnant donc
ses parties correspondantes pour modeliser des commandes avec les 
differents capteurs et signaux.
Controller Training:
 Dans cette fonction on retouve la complete manipulation des classes pour l'entrainement
 - Deduction d'apres le niveau de l'utilisateur le type de programme a faire
 - Retour de l'ensemble des composantes de l'entrainement ainsi que ses procedées
 - Enregistrement d'informations liées a l'entrainement
 - Fonctionnement parellele avec le controller Robot
"""
#Constantes Parametriques:
CONST_PATH_TRAININGS = './Training/'

#BASE DE DONNES A REMPLACER:

#Type d'entrainement installé
ProgramList = ['ExerciceWithStrike','RobotTrainSparbar','RobotTrain','Exercice','Main']

#Niveaux Installes 
Levels = ['A','B','C']

#***********FIN BASE DE DONNEES********
"""
DURING DEVELOPPEMENT
"""
us = {'User': 'Sad', 'Level':'A'}

#Implementation des modules et librairies Python
import re
import asyncio
import os

#Implementation des differents composants

import classProgram as Program
import classIA as IA
import classTraining as Training

class ControllerTraining:
    ProgramsList = {}
    def __init__(self,Training,dUser,aParams = []):
        self.User = dUser
        self.Trains = self.loadTrains()
        if (Training == "ExerciceWithStrike"):
            self.controllerExerciceWithStrike(aParams)
        elif (Training == "RobotTrainSparbar"):
            self.controllerRobotTrainSparbar(aParams)
        elif (Training == "RobotTrain"):
            self.controllerRobotTrain(aParams)
        elif (Training == "Main"):
            self.controllerMain(aParams)
        elif (Training == "Exercic"):
            self.controllerExercice(aParams)
        else:
            #Remplace par module Error Not Train
            print("Error")
    def loadTrains(self):
        Files = os.listdir(CONST_PATH_TRAININGS)
        for file in Files:
            self.ProgramsList[(file.strip('.aee'))] = Program.Program((CONST_PATH_TRAININGS + file) ,self.User['Level'],ProgramList,Levels)
        

    def controllerMain(self, aParams): return
    def controllerRobotTrain(self, aParams): return
    def controllerRobotTrainSparbar(self, aParams): return
    def controllerExerciceWithStrike(self, aParams): return
    def controllerExercice(self, aParams): return 




var = ControllerTraining('Main', us)
print(var.ProgramsList['ShadowBoxing'].UserDefault)
