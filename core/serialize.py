
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

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

