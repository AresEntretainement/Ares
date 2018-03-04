#ModulesInstalled = ['Test','TechnicalVelocity','TechnicalPower','Squat','Sparring','ShadowBoxing','Pompes','CordeSauter','Burpees','Pao']
from controllers.controllerDB import ControllerDB
d = ControllerDB()
ModulesInstalled = d.getExercicesInstalled()