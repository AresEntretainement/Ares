file = open('ShadowBoxing.aee','r')
import re
Dict = {}
FieldExpression = '(.)*:(.)*'

for line in file:
	print line
	if (re.search(FieldExpression, line) is not None):
		 Field = re.search(FieldExpression, line).group(0).strip('\n').split(':')
		 Dict[Field[0]] = Field[1]
	else:
		pass

print Dict

