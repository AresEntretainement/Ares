from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import hashlib
from random import randint
from constants import PARAM_SALT, PARAM_CUSTOM_HASH_SALT

class Hash:

	algorithms = ['md5','sha1','sha224','sha256','sha384','sha512']
	def init(self):
		self.algorithms = algorithms
	def md5(self,sHash):
		return hashlib.md5(str.encode(sHash)).hexdigest()
	def sha1(self,sHash):
		return hashlib.sha1(str.encode(sHash)).hexdigest()
	def sha224(self,sHash):
		return hashlib.sha224(str.encode(sHash)).hexdigest()
	def sha256(self,sHash):
		return hashlib.sha256(str.encode(sHash)).hexdigest()
	def sha384(self,sHash):
		return hashlib.sha384(str.encode(sHash)).hexdigest()
	def sha512(self,sHash):
		return hashlib.sha512(str.encode(sHash)).hexdigest()

	def getPassHash(self, sPassword):
		if (PARAM_CUSTOM_HASH_SALT):
			sPassword = sPassword + PARAM_SALT
		sSeed = ''
		substr = '0123456789abcdef'
		for i in range(0,10):
			randomInt = randint(0, len(substr)-1)
			sSeed += substr[randomInt]
		return self.sha256(sSeed + self.md5(sPassword) + sSeed) + sSeed

	def comparePassHash(self, sPassword, sStoredValue):
		if (PARAM_CUSTOM_HASH_SALT):
			sPassword = sPassword + PARAM_SALT
		if (len(sStoredValue) < 64):
			return False
		sStoredSeed = sStoredValue[64 : 74]
		if ((self.sha256(sStoredSeed + self.md5(sPassword) + sStoredSeed) + sStoredSeed) == sStoredValue):
			return True
		else:
			return False

	def compareFields(self, sCodage, sPassword, sCompare):
		if (sCodage in self.algorithms):
			if(eval("self." + sCodage + "('" + sCompare + "')") == sPassword):
				return True
			else:
				return False
		else:
			return False


