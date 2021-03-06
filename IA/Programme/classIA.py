import numpy as np
#Algoriths Disponibility:
AlgorithmsInstalled = ['RegressionAlgorithm','RuffierDickson']
TypeExercices = ['ExerciceCardioVascular','ExerciceMuscular']

class IA:
    def __init__(self,RecopilationTraining, TypeIA):
        self.Infos = RecopilationTraining
        self.Infos = self.Process(self.Infos, TypeIA)

    def Process(self, Infos, TypeIA):
        if (TypeIA == 'RuffierDickson'):
            return Infos['ExerciceCardioVascular']

        elif (TypeIA == 'RegressionAlgorithm'):
            pass

    def RegressionAlgorithm(self):
        return 'RegressionAlgo'
        


    def RuffierDickson(self, aParams = {}):
        if (aParams == None or aParams == {}):
            aParams = self.Infos['Perf']
        Categories = {
                        'Exellence' : 'NV',
                        'Very_Good' : {'Max' : 0 , 'Min' : 2},
                        'Good'      : {'Max' : 2 , 'Min' : 4},
                        'Normal'    : {'Max' : 4 , 'Min' : 6},
                        'Bad'       : {'Max' : 6 , 'Min' : 8},
                        'Very_Bad'  : {'Max' : 8 , 'Min' : 10},
                    'Not_Adapted'   : {'Maxed' : 10}
                    }
        Keys = ['Fc0', 'Fc1', 'Fc2']
        if (len(aParams.keys()) != len(Keys)):
            #Remplace for Error type Algorithm Params Are Not Ideal
            print('Error : TYPE ALGORITH DICKSON NOT IDEAL PARAMS')
            return
        for key in aParams.keys():
            if (key not in Keys):
                #Remplace for Error type Algorithm Params not ideal Keys
                print('Error : TYPE ALGORITH DICKSON NOT GOOD KEYS')
                return
        ValueCorrelation =  ( ( ( int( aParams['Fc1'] ) - 70 ) + (2 * ( int(aParams['Fc2']) - int(aParams['Fc0']) )) ) / (10) )
        CorrelationCategorie = ''
        for key in Categories.keys():
            if(Categories[key] == 'NV'):
                if (ValueCorrelation < 0):
                    CorrelationCategorie = key 
            else:
                if ('Maxed' in Categories[key].keys()):
                    if (ValueCorrelation > Categories[key]['Maxed']):
                        CorrelationCategorie = key
                else:
                    if( Categories[key]['Max'] < ValueCorrelation <= Categories[key]['Min']):
                        CorrelationCategorie = key

        return [ValueCorrelation, CorrelationCategorie]

Train = {1: {'Library': 'performanceLibBurpees', 'Performance': '52', 'Training': 'Burpees'}, 2: {'Library': 'performanceLibBurpees', 'Performance': '52', 'Training': 'Burpees'}}
Ruff = {'Fc0' : 72, 'Fc1' : 120, 'Fc2' : 90}
RuffHamza = {'Fc0' : 66, 'Fc1' :  102, 'Fc2' :  84}
Test = {'Fc0' : 56, 'Fc1' : 65, 'Fc2' : 57}
