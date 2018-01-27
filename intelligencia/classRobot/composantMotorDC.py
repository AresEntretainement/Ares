from . import export
import RPi.GPIO as GPIO
from time import sleep
import asyncio

@export
class MotorDC:
    RequiredElements = ['Type','NumberPorts','Utilisation','PortNames']
    def __init__(self,Configuration):
        for conf in self.RequiredElements:
            if(conf not in Configuration.keys()):
                print('Error')
                assert Exception
        self.Type = Configuration['Type']
        self.NumberOfPorts = Configuration['NumberPorts']
        for port in Configuration['PortNames']:
            Query = "self."+port + " = " + Configuration[port]
            exec(Query)

## Controle d'un moteur DC par le Raspberry Pi



GPIO.setmode(GPIO.BOARD)   ##apparemment y a une différence de syntaxe entre BCM et BOARD, mais vu que j'ai pas compris, j'propose qu'on laisse et qu'on fasse genre "ouais c'est pour exploiter au mieux Python"

Moteur1A = 16      ## premiere sortie du premier moteur, pin 16
Moteur1B = 18      ## deuxieme sortie de premier moteur, pin 18
Moteur1E = 22      ## enable du premier moteur, pin 22

GPIO.setup(Moteur1A,GPIO.OUT)  ## ces trois pins du Raspberry Pi sont des sorties
GPIO.setup(Moteur1B,GPIO.OUT)
GPIO.setup(Moteur1E,GPIO.OUT)

async def moteur(self):

    pwm = GPIO.PWM(Moteur1E,50)   ## pwm de la pin 22 a une frequence de 50 Hz
    pwm.start(20)   ## on commence avec un rapport cyclique de 20% => accélération vers 50% puis 100% pour pas que le moteur soit en position "appelez les hendeks"

    GPIO.output(Moteur1A,GPIO.HIGH)
    GPIO.output(Moteur1B,GPIO.LOW)
    GPIO.output(Moteur1E,GPIO.HIGH)

    sleep(0.2)

    pwm.ChangeDutyCycle(50)  ## modification du rapport cyclique a 50%

    sleep(0.2)

    pwm.ChangeDutyCycle(100) ## modification du rapport cyclique à 100%

    sleep(5) ## temporisation avant de couper le moteur et arrêter la sparbat, à redéfinir

    GPIO.output(Moteur1E,GPIO.LOW)

    pwm.stop()    ## interruption du pwm

    GPIO.cleanup()