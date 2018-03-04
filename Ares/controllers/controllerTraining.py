#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Partie du programme qui Enchaine le programme d'entrainement
d'apres le niveau obtenu lors de l'evaluation en selectionnant donc
ses parties correspondantes pour modeliser des commandes avec les 
differents capteurs et signaux.
Controller Training:
 Dans cette fonction on retouve la complete manipulation des classes pour l'entrainement
 - Deduction d'apres le niveau de l'utilisateur le type de programme a faire
 - Retour de l'ensemble des composantes de l'entrainement ainsi que ses procedées
 - Enregistrement d'informations liées a l'entrainement
 - Fonctionnement parellele avec le controller Robot
"""
"""
Classe Capable de lire l'ensemble des programmes installées
Categorie de Programmes
: ExerciceMuscular
: ExerciceCardioVascular
: ExerciceWithStrike
: RobotTrainSparbar
: RobotTrain
: ExerciceStart (Echauffement)

#Section temporaire pour la modelisation (EVALUATION PROTYPE)
-------------------------------------------
FIELDS : Objects = /Proprieties,DefaultValues,Fields=Empty/
Proprieties : PREFIX ; TITLE ; TYPE ; EVALUATION ; CONTROLLER
DefaultValues : DefaultPause ; DefaultTimeRound ; DefaultRounds



"""


#***********FIN BASE DE DONNEES********
"""
DURING DEVELOPPEMENT
"""
#EvaluationTraining = { 1 : 'ShadowBoxing', 2 : 'CordeSauter', 3 : 'Pompes' , 4 : 'Squat' , 5 : 'Burpees', 6 : 'TechnicalPower' , 7 : 'TechnicalVelocity' , 8 : 'Pao' , 9 : 'Sparring'}
EvaluationTraining = {1 : 'Burpees', 2 : 'Burpees'}

#Implementation des modules et librairies Python
import re
import asyncio
import os
import time
#Implementation des differents composants
from classes.classIA import IA
from classes.classTraining import Train

class ControllerTraining:
    ProgramsList = {}
    def __init__(self,dUser,aParams = [],Training = EvaluationTraining):
        self.User = dUser
        if (Training == EvaluationTraining):
            self.EvaluationMode = True
        self.Training = Train(Training,self.EvaluationMode)

    def run(self):
        Results = {}
        for index in range(1,len(self.Training.TrainingParties)+1):
            Results[index] = {}
        for index in range(1,len(self.Training.TrainingParties)+1):
            self.Training.TrainingParties[index].Controller.run()
            Perfs = {}
            Perfs = self.Training.TrainingParties[index].Controller.getPerformances()
            Results = {}
            for exercice in Perfs.keys():
                if(Perfs[exercice]['Type'] not in IA.AlgorithmsInstalled):
                    #Remplace for Error Algorithm of Complement Not installed
                    print('Error : ALGORITH OF COMPLEMENT NOT INSTALLED')
                else:
                    Intelligencia = IA(Perfs, Perfs[exercice]['Type'])
                    Query = "Results['" + exercice + "'] = Intelligencia." + Perfs[exercice]['Type']  + "()"
                    exec(Query)
                    time.sleep(2)
            print(Results)
