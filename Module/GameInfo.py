#!/usr/bin/env python
"""***************************************************************
**  Program Name:   BGGStatus				        **
**  Version Number: V0.6                                        **
**  Copyright (C):  September 3, 2014 Richard W. Allen          **
**  Date Started:   September 3, 2014                           **
**  Date Ended:     May 15, 2019                                **
**  Author:         Richardn W. Allen                           **
**  Webpage:        http://www.richardallenonline.com           **
**  IDE:            IDLE 3.6.5                                  **
**  Compiler:       Python 3.6.5                                **
**  Langage:        Python 3.6.5				**
**  License:	    GNU GENERAL PUBLIC LICENSE Version 2	**
**		    see license.txt for for details	        **
***************************************************************"""
import os
import math
import sys
sys.path.append('Module.zip')

class GameInfo:
    def __init__(self, name):
        self.name = name
        self.win = 0
        self.loss = 0
        self.count = 0

    def AddCount(self, win):
        if (win == True):
            self.win += 1
        else:
            self.loss += 1
        self.count += 1

if __name__ == "__main__":
    pass
