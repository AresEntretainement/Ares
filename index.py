# -*-coding:utf-8 -*-
"""
[ARES PROJECT]
* @copyright		[ARES ENTRETAINEMENT]
* @author			CHOUBIKI Ismael
* @package 			AresTrain
* @version 			$id: index.py
*
*
"""
"""
[Import Modules Python]

[Description]
- Module sys
"""

from constants import *




# Require Ares Class Initialisation

from classes.classAres import *

defined(CONST_ARES)

objectTest = Ares()
#print objectTest.getVersion()

Test = Ares()
print Test.getPhrase('hell','FR')






