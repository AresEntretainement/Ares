
us = {'User': 'Sad', 'Level':'A'}
#EvaluationTraining = { 1 : 'ShadowBoxing', 2 : 'CordeSauter', 3 : 'Pompes' , 4 : 'Squat' , 5 : 'Burpees', 6 : 'TechnicalPower' , 7 : 'TechnicalVelocity' , 8 : 'Pao' , 9 : 'Sparring'}



from controllers.controllerTraining import ControllerTraining




Contoller = ControllerTraining(us)
Contoller.run()
#Contoller.run()
robot = Contoller.Training.TrainingParties[1].ElementController['ExerciceCardioVascular']


robot.do(
    [
        robot.useModule('UltrasonGaucheTorse','mesureForce',10,0,[1]),
        robot.useModule('MoteurSparBar','turnSpeed',10,1,[2])
    ]
)

