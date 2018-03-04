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

    GPIO.setmode(GPIO.BOARD)              # GPIO Numbering

    GPIO.setup(3, GPIO.OUT)

    # pin 3 à 50Hz
    pwm = GPIO.PWM(3, 50)

    # cycle 0 comme ça aucun angle par défaut lors du démarrage
    pwm.start(0)

    async def SetAngle(angle):

        duty = angle / 18 + 2

        GPIO.output(03, True)

        pwm.ChangeDutyCycle(duty)

        sleep(1)

        GPIO.output(03, False)

        pwm.ChangeDutyCycle(0)

    SetAngle(90)

    pwm.stop()

    GPIO.cleanup()
