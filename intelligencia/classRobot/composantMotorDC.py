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

        GPIO.setmode(GPIO.BCM)              # GPIO Numbering

        OutLine = 16      ## premiere sortie du premier moteur, pin 16
        AlphaRaport = 18      ## deuxieme sortie de premier moteur, pin 18
        Truc = 22      ## enable du premier moteur, pin 22

        GPIO.setup(self.OutLine,GPIO.OUT)  # All pins as Outputs
        GPIO.setup(self.AlphaRaport,GPIO.OUT)
        GPIO.setup(self.Truc,GPIO.OUT)

    async def moteur(self, pause): 



            GPIO.output(self.OutLine,GPIO.HIGH)
            GPIO.output(self.AlphaRaport,GPIO.LOW)
            GPIO.output(self.Truc,GPIO.HIGH)
 
            sleep(pause)
            # Stop
            GPIO.output(self.Truc,GPIO.LOW)

            GPIO.cleanup()
