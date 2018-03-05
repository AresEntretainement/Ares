from . import export
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
        if isinstance(Configuration['PortNames'], list):
            for port in Configuration['PortNames']:
                Query = "self."+port + " = " + Configuration[port]
                exec(Query)
        else:
            Query = "self." + Configuration['PortNames'] + " = " + Configuration[Configuration['PortNames']]
            exec(Query)
    async def turnSpeed(self,x):
        print('Turning..')
        await asyncio.sleep(x)
        print('Stop Turning')
        return 'Turned'
