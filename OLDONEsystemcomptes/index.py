from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pickle
import sqlite3
import os
import time

from controllers.controllerDB import ControllerDB 
from classes.classHash import Hash


Controller = ControllerDB()

def main():
    User = input("Nom d'utilisateur >")
    Pass = input("Password >")
    if(Controller.verifyPass(User, Pass)):
    	print(Controller.searchTrainigsUser(User))
    	print("\n")
    	print(Controller.getFieldUser(User, '*'))
    else:
        print("ERRONéé")
        time.sleep(2)
        main()
    return

main()
