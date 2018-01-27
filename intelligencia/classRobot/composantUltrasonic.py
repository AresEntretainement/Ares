from . import export
import RPi.GPIO as GPIO
import time
import asyncio



@export

class Ultrasonic:
    ValuesCharge = {}
    ListTest = []
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

        ###SETUP OF ULTRASONIC MODULE###
        # Use BCM GPIO references
        # instead of physical pin numbers
        GPIO.setmode(GPIO.BCM)


        # Set pins as output and input
        GPIO.setup(self.Trigg,GPIO.OUT)  # Trigger
        GPIO.setup(self.Echo,GPIO.IN)    # Echo

    async def mesureForce(self, pause):

        # Set trigger to False (Low)
        GPIO.output(self.Trigg, False)

        # Allow module to settle
        time.sleep(pause)

        # Send 10us pulse to trigger
        GPIO.output(self.Trigg, True)
        time.sleep(pause)
        GPIO.output(self.Trigg, False)
        start = time.time()
        while GPIO.input(self.Echo)==0:
          start = time.time()

        while GPIO.input(self.Echo)==1:
          stop = time.time()

    distance = allerRetour * 34029 # parce qu'on est précis

    distance = distance / 200

    print "Distance : %.1f" % distance

    #partie pour prendre la force à partir de la distance
    distanceInit = 12
    distanceParcourue = distanceInit - distance
    print "La distance parcourue est de : %1.f cm" % distanceParcourue
    # K = 3.913N/mm soit 39.13N/cm => distance en cm donc conversion de K
    # Autre méthode est de faire 3.913 * distanceParcourue 
    force = 39.13 * distanceParcourue
    print "La force du coup est de : %1.f N" % force 
        
        self.ListTest.append(force)

        await asyncio.sleep(pause)
        return 'Mesure Token'
