import pyglet
import datetime
import os

from pyglet.window import key



window = pyglet.window.Window()
dateInit = datetime.datetime.now()

compter = 0

def registe(coup):
	global dateInit
	datebaseFile = 'database.aee'
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
		return True
	elif symbol == key.Q:
	    print('CrochetG')
	    registe('CrochetG')
	    return True
	elif symbol == key.S:
	    print('UpperCutG')
	    registe('UpperCutG')
	    return True
	elif symbol == key.O:
	    print('Cross')
	    registe('Cross')
	    return True
	elif symbol == key.M:
	    print('CrochetD')
	    registe('CrochetD')
	    return True
	elif symbol == key.L:
	    print('UpperCutD')
	    registe('UpperCutD')
	    return True
	return False

pyglet.app.run() 