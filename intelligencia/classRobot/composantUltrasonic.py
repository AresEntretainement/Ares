from . import export
#import RPi.GPIO as GPIO
import time
import asyncio

"""

import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO = 24

print "Ultrasonic Measurement"

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

# Allow module to settle
time.sleep(0.5)

# Send 10us pulse to trigger
GPIO.output(GPIO_TRIGGER, True)
time.sleep(0.00001)
GPIO.output(GPIO_TRIGGER, False)
start = time.time()
while GPIO.input(GPIO_ECHO)==0:
  start = time.time()

while GPIO.input(GPIO_ECHO)==1:
  stop = time.time()

# Calculate pulse length
elapsed = stop-start

# Distance pulse travelled in that time is time
# multiplied by the speed of sound (cm/s)
distance = elapsed * 34000

# That was the distance there and back so halve the value
distance = distance / 2

print "Distance : %.1f" % distance

# Reset GPIO settings
GPIO.cleanup()



"""




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
        #GPIO.setmode(GPIO.BCM)
    async def takeMesure(self,x):
        print('Taking Mesure')
        for i in range(100):
            self.ListTest.append(i)


        await asyncio.sleep(x)
        print('Mesure Token')
        return 'Mesure Token'
