"""
import hashlib
hash_object = hashlib.md5(b'Hello World')
print(hash_object.hexdigest())

import pickle

#Here's an example dict
grades = { 'Alice': 89, 'Bob': 72, 'Charles': 87 }

#Use dumps to convert the object to a serialized string
serial_grades = pickle.dumps( grades )
print type(serial_grades)
print serial_grades
#Use loads to de-serialize an object
received_grades = pickle.loads( serial_grades )
print type(received_grades)
#print received_grades
"""
"""
sys.path.append('path/to/app') # *nix path
# equivalent de 'from modules import module', mais, pour le coup, dynamique
t# voir la doc : http://docs.python.org/library/functions.html#__import__ 
""" 
aParams=["'hello'"]


sClass = 'Hello'
cmd = sClass + '('

for i in range(len(aParams)):
	cmd += aParams[i]
	if (i != len(aParams)-1):
		cmd+= ','
cmd += ')'

print cmd

