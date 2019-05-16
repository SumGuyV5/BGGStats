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
import sys
import datetime
sys.path.append('Module.zip')

from Module.PlayerDataset import PlayerDataset

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
