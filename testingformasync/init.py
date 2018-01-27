import asyncio

class Ultrason:
    async def takeMesure(self,x):
        print('Taking Mesure')
        await asyncio.sleep(x)
        print('Mesure Token')
        return 'Mesure Token'





class Robot:
    Robot = {'Ultra':Ultrason()}
    Tasks = []
    async def _useModule(self,Mod,Method = "run",Requests = 1,Sleep = 0, aParams=[]):
        tasks = []
        if(Mod not in self.Robot.keys()):
            #Module Dont exist Remplace Error
            print("Error")
        else:
            if(Method in dir(self.Robot[Mod])):
                sParams = str(aParams).strip("[")
                sParams = sParams.strip("]")

                for idx in range(1, Requests+1):
                    Query = "self.Robot['" + Mod + "']." + Method + "(" + sParams + ")"
                    print(Query)
                    tsk = asyncio.ensure_future(eval(Query))
                    self.Tasks.append(tsk)
                    asyncio.sleep(Sleep)
            else:
                #Replace for Module Error, Method Composant Dont Exist
                print("Error h")

    async def _do(self):
        await asyncio.wait(
            [
                self._useModule('Ultra','takeMesure',10,0,[2]),
                self._useModule('Ultra','takeMesure',10,1,[6])
            ]
        )
    def do(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._do())

    def run(self):
        Loop = asyncio.get_event_loop()
        Loop.run_until_complete(asyncio.gather(*self.Tasks))

Rob = Robot()

Rob.do()
Rob.run()