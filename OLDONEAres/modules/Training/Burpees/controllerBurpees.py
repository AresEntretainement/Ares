#Required classTimer
import os
import importlib
import asyncio
import time
from classes.classTimerExercice import _Timer
from constants import CONST_PRINT, CONST_TIME_SLEEP_CARDIO_MESURE, CONST_COEFF_CARDIO_MESURE, CONST_TRAINING
INSTALL_PACKAGE_INFOS = ['Proprieties','DefaultValues','Algorithm','Field','Image','Description','Buttons','LibPerformance','Questions','Default','LibPause','LibTimeRound','PerformanceIndex','LibRounds']
####VALUE IN CONSTANT SETTINGS

class Burpees:
    def __init__(self,GeneralLib,Level = 'Eval'):
        self.Level = Level
        self.Doc = GeneralLib
        self.Performance = {}
        for key in self.Doc.keys():
            if (key == 'Field'):
                for newKey in self.Doc['Field']:
                    Query = "self." + newKey + " = " + str(self.Doc['Field'][newKey]) 
                    exec(Query)
                    for insideKey in self.Doc['Field'][newKey].keys():
                        if (isinstance(self.Doc['Field'][newKey][insideKey], dict)):
                            Queryed = "self." + insideKey + " = " + str(self.Doc['Field'][newKey][insideKey])
                        elif(self.Doc['Field'][newKey][insideKey].isdigit()):
                            Queryed = "self." + insideKey + " = " + str(self.Doc['Field'][newKey][insideKey])
                        else:
                            Queryed = "self." + insideKey + " = '" + str(self.Doc['Field'][newKey][insideKey] + "'")
                        exec(Queryed)
            else:
                Query = "self." + key + " = " + str(self.Doc[key]) 
                exec(Query)
                for insideKey in self.Doc[key].keys():
                    if(isinstance(self.Doc[key][insideKey], (int))):
                        Queryed = "self." + insideKey + " = " + str(self.Doc[key][insideKey])
                    elif (isinstance(self.Doc[key][insideKey] , list)):
                        Queryed = "self." + insideKey + " = " + str(self.Doc[key][insideKey]) 
                    else:
                        Queryed = "self." + insideKey + " = '" + str(self.Doc[key][insideKey] + "'")
                    exec(Queryed)
        self.Img = self.getImage()
        self.Header = self.printExercice()
    def getImage(self):
        imageModule = importlib.import_module('.'+self.Image.replace(".py",''), str(CONST_TRAINING+'.'+self.Prefix))
        return imageModule.Image
    def printExercice(self):
        Print = """
        
        -----------------------------------------------------------------
                                 {0}
        {1}
        --Image----------------------------------------------------------
        {2}
        """.format(self.Title,self.Description,self.Img)
        return Print

    def affichage(self):
        print(self.Title)
        print(self.Prefix)

    def setPerformance(self):
        Reps = input('Rentrez Performance : > ')
        input('Mesurez Votre poux apres enter jusqua notification...')
        time.sleep(CONST_TIME_SLEEP_CARDIO_MESURE)
        print('Fini')
        self.Performance['Fc1'] = ( 6 * int(input('Rentrez votre pouls > ')) )
        print('Maintenant Prenez un repos de 1min avant une autre mesure')
        time.sleep(60)
        input('Mesurez Rapidement Votre poux apres enter jusqua notification...')
        time.sleep(CONST_TIME_SLEEP_CARDIO_MESURE)
        print('Fini')
        self.Performance['Fc2'] = ( 6 * int(input('Rentrez votre pouls > ')) )
        self.PerformanceReps = Reps
        return 
        
    def getPerformances(self):
        Perf = {}
        for exercice in self.Type:
            if(exercice == 'ExerciceCardioVascular'):

                Perf['ExerciceCardioVascular'] = {
                                            'Perf' : self.Performance,
                                            'Type' : self.ExerciceCardioVascularAlgorithm,
                                            'Lib' : 'Empty'
                                            }
            elif(exercice == 'ExerciceMuscular'):

                Perf['ExerciceMuscular'] = {
                                                    'Perf' : self.PerformanceReps,
                                                    'Type' : self.ExerciceMuscularAlgorithm,
                                                    'Lib' : self.PerformanceLib
                                                }

        return Perf
    def PauseInput(self):
        input("...")
        return
    def run(self):
        if (self.Level == 'Eval'):
            input("Mesurez votre pouls apres enter jusqu'a notification..")
            time.sleep(CONST_TIME_SLEEP_CARDIO_MESURE)
            print('Fini')
            self.Performance['Fc0'] = ( 6 * int(input('Rentrez votre pouls > ')) )
            self.Timer = _Timer(self.Header,CONST_PRINT,float(int(self.DefaultTimeRound)), self.setPerformance)
            self.Timer.start()
            self.Pause = _Timer("           Pause           ",CONST_PRINT,float(int(self.DefaultPause)), self.PauseInput)
            self.Pause.start()
        else:
            pass

        return


