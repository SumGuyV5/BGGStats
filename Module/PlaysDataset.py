#!/usr/bin/env python
"""***************************************************************
**  Program Name:   BGG	     				        **
**  Version Number: V0.5                                        **
**  Copyright (C):  September 3, 2014 Richard W. Allen          **
**  Date Started:   September 3, 2014                           **
**  Date Ended:     September 3, 2014                           **
**  Author:         Richardn W. Allen                           **
**  Webpage:        http://www.richardallenonline.com           **
**  IDE:            IDLE 2.7.4                                  **
**  Compiler:       Python 2.7.4                                **
**  Langage:        Python 2.7.4				**
**  License:	    GNU GENERAL PUBLIC LICENSE Version 2	**
**		    see license.txt for for details	        **
***************************************************************"""
import sys
import datetime
sys.path.append('Module.zip')

from PlayerDataset import PlayerDataset

class PlaysDataset:
    def __init__(self):
        self.gamename = ""
        self.length = 0
        self.location = ""
        self.incomplete = 0
        self.nowinstate = 0
        self.players = []
        self._date = datetime.date.today()

    def AddPlayer(self, player):
        self.players.append(player)

    def date(self, string):
        self._date = datetime.datetime.strptime(string, "%Y-%m-%d")
        

if __name__ == "__main__":
    pass
