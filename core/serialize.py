import pickle

class Os:
	name = 'mon nom'
	def __init__(self):
		return

def serialize(oObject = None):
	if (oObject == None):
		return ''

	return pickle.dumps(oObject)

def deserialize(sString):
	return pickle.loads(sString)

d = Os()
print d 
a = serialize(d)
b = deserialize(a)
print b.name

