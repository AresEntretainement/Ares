import pyglet
import datetime
import os

from pyglet.window import key



window = pyglet.window.Window()
dateInit = datetime.datetime.now()
datebaseFile = 'database.aee'
compter = 0

def registe(coup):
	global dateInit,datebaseFile

	file = open(datebaseFile,'a')

	datet = coup + '=' +  str(datetime.datetime.now()-dateInit) + '\n'
	dateInit = datetime.datetime.now()
	file.write(datet)
	os.system('clear')
	





@window.event
def on_key_press(symbol, modifiers):
	global compter, dateInit

	if symbol == key.Z:
		if(compter == 0):
			dateInit = datetime.datetime.now()
		print('Jab')
		registe('Jab')
		compter += 1 
		return True
	elif symbol == key.Q:
	    print('CrochetG')
	    registe('CrochetG')
	    compter += 1 
	    return True
	elif symbol == key.S:
	    print('UpperCutG')
	    registe('UpperCutG')
	    compter += 1 
	    return True
	elif symbol == key.O:
	    print('Cross')
	    registe('Cross')
	    compter += 1 
	    return True
	elif symbol == key.M:
	    print('CrochetD')
	    registe('CrochetD')
	    compter += 1 
	    return True
	elif symbol == key.L:
	    print('UpperCutD')
	    registe('UpperCutD')
	    compter += 1 
	    return True
	elif symbol == key.SPACE:
		print('Pause...')
		input('...')
		dateInit = datetime.datetime.now()
		return True
	return False

enter = input('Enter File')
if ('.aee' in enter):
	datebaseFile = enter
	d = open(datebaseFile,'w')
	d.close()



pyglet.app.run() 