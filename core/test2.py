
try:
	raise Exception('spam', 'eggs')
except Exception as inst:
	print type(inst)     # the exception instance
	print inst.args      # arguments stored in .args
	print inst           # __str__ allows args to be printed directly
	x, y = inst.args
	print 'x =', x
	print 'y =', y