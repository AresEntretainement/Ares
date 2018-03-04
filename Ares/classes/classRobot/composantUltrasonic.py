<<<<<<< HEAD:Ares/classes/classRobot/composantUltrasonic.py
from . import export
#import RPi.GPIO as GPIO
import time
import asyncio



@export

class Ultrasonic:
    """
    ValuesCharge = {}
    ListTest = []
    """
    RequiredElements = ['Type','NumberPorts','Utilisation','PortNames']

    def __init__(self,Configuration):
        for conf in self.RequiredElements:
            if(conf not in Configuration.keys()):
                print('Error')
                assert Exception
        self.Type = Configuration['Type']
        self.NumberOfPorts = Configuration['NumberPorts']
        if isinstance(Configuration['PortNames'], list):
            for port in Configuration['PortNames']:
                Query = "self."+port + " = " + Configuration[port]
                exec(Query)
        else:
            Query = "self." + Configuration['PortNames'] + " = " + Configuration[Configuration['PortNames']]
            exec(Query)
    async def mesureForce(self,x):
        print('Taking Mesure..')
        await asyncio.sleep(x)
        print('Mesure Token')
        return 'Mesured'

"""
        ###SETUP OF ULTRASONIC MODULE###
        # Use BCM GPIO references
        # instead of physical pin numbers
        GPIO.setmode(GPIO.BCM)

        
        print "Ultrasonic Measurement"

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
        while GPIO.input()==0:
          start = time.time()

        while GPIO.input(self.Echo)==1:
          stop = time.time()

        # Calculate pulse length
        elapsed = stop-start

        # Distance pulse travelled in that time is time
        # multiplied by the speed of sound (cm/s)
        distance = elapsed * 34000

        # That was the distance there and back so halve the value
        distance = distance / 2

        #partie pour prendre la force à partir de la distance
        distanceInit = 12
        distanceParcourue = distanceInit - distance
        force = 3.913 * distanceParcourue
        
        self.ListTest.append(force)

        await asyncio.sleep(pause)
        return 'Mesure Token'
"""
=======
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
>>>>>>> 9eb6ff285d28c744655e19222922a2fbedadf60e:intelligencia/classRobot/composantUltrasonic.py
