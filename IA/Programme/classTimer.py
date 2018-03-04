import datetime
import asyncio
import time
from threading import Timer
import os

class _Timer:
	def __init__(self,Header,IsPrint,iTime,func, args = [], kwargs = {}):
		""" SECURITY TIME """
		self.iTime = iTime + 1
		self.t = Timer(self.iTime, func, args, kwargs)

		self.Header = Header
		self.iTimeOriginal = iTime
		if (IsPrint):
			self.IsPrint = True 
	def start(self):
		if(self.IsPrint):
			self.time = Timer(0,self.print,[self.Header])
			self.t.start()
			self.time.start()
			print('In')
			self.time.join()
			self.t.join()
		else:
			self.t.start()
			self.t.join()
			self.t.cancel()
			
		return 
	def print(self,Header):
		while ((int(self.iTime)-2) > -1):
			print(Header)
			print("Time Is : " + str(self.iTimeOriginal))
			print('Rest : '+str(self.iTime))
			time.sleep(1)
			os.system('cls' if os.name == 'nt' else 'clear')
			self.iTime -= 1 
		print(Header)
		print("Is Finish")

