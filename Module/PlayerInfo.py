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

from Module.PlaysDataset import PlaysDataset
from Module.PlayerDataset import PlayerDataset

class PlayerInfo:
    def __init__(self, name, username):
        self.name = name
        self.username = username
        self.wincount = 0
        self.losscount = 0
        self.winratio = 0.0
        self.winpercentage = 0.0
        self.gameInfo = []
        self.hIndex = 0
        self.winGameInfo = object()
        self.lossGameInfo = object()

    def LoadGameInfo(self):
        self.gameInfo = sorted(self.gameInfo, key=lambda gameInfo: gameInfo.win, reverse = True)
        self.winGameInfo = self.gameInfo[0]
        self.gameInfo = sorted(self.gameInfo, key=lambda gameInfo: gameInfo.loss, reverse = True)
        self.lossGameInfo = self.gameInfo[0]
        self.gameInfo = sorted(self.gameInfo, key=lambda gameInfo: gameInfo.count, reverse = True)
        count = 0
        while count < self.gameInfo.__len__():
            if (self.gameInfo[count].count <= count):
                break
            count += 1
        self.hIndex = count

if __name__ == "__main__":
    pass
