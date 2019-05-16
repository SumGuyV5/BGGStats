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

from Module.PlaysDataset import PlaysDataset
from Module.PlayerDataset import PlayerDataset
from Module.PlayerInfo import PlayerInfo
from Module.ReadXML import ReadXML
from Module.DownloadXML import DownloadXML
from Module.GameInfo import GameInfo

class BGGStats:
    def __init__(self):
        self.pagesize = 100
        self.username = "SumGuyV5"
        
        self.url = "http://www.boardgamegeek.com/xmlapi2/plays?username=" + self.username + "&pagesize=" + str(self.pagesize) + "&page="
        self.filename = "plays.xml"

        self.plays = []
        self.playersInfo = []
        
        self.downloadXML = DownloadXML(self.url, self.filename)
        self.readXML = ReadXML()

    def Main(self):
        count = 1
        countto = 1
        while (count <= countto):
            self._Download(count)
            self._Read()
            countto = math.ceil(self.readXML.playcount / float(self.pagesize))
            count += 1
            
        self._LoadInfo()
        self._WinPercentage()
        self._SortPlayers("winpercentage")
        self._Print()

    def _LoadInfo(self):
        for play in self.plays:
            if (play.incomplete == 0) and (play.nowinstate == 0):
                for player in play.players:
                    if (self._AddPlayer(player.username, player.name, player.win, play.gamename) == False):
                        print("Error Player not found!")

    def _AddPlayer(self, username, name, win, gameName):
        found = False
        for playerInfo in self.playersInfo:
            if ((playerInfo.username == username) and (playerInfo.name == name)):
                found = True
                self._AddGameInfo(gameName, win, playerInfo)
                if (win == True):
                    playerInfo.wincount += 1
                else:
                    playerInfo.losscount += 1
        if ( found == False ):
            self.playersInfo.append(PlayerInfo(name, username))
            found = self._AddPlayer(username, name, win, gameName)

        return found

    def _AddGameInfo(self, name, win, playerInfo):
        found = False
        for gameInfo in playerInfo.gameInfo:
            if (gameInfo.name == name):
                found = True
                gameInfo.AddCount(win)
        if ( found == False ):
            playerInfo.gameInfo.append(GameInfo(name))
            found = self._AddGameInfo(name, win, playerInfo)
                
        
            

    def _Download(self, number):
        self.downloadXML.url = self.url + str(number)
        self.downloadXML.Download()

    def _Read(self):
        self.readXML.ReadXMLFile(os.getcwd() + '\\' + self.filename)
        self.plays = self.readXML.plays

    def _SortPlayers(self, sortby):
        if (sortby == "wincount"):
            self.playersInfo = sorted(self.playersInfo, key=lambda playersInfo: playersInfo.wincount, reverse = True)
        elif (sortby == "winpercentage"):
            self.playersInfo = sorted(self.playersInfo, key=lambda playersInfo: playersInfo.winpercentage, reverse = True)

    def _Print(self):
        for player in self.playersInfo:
            player.LoadGameInfo()
            print ("\n")
            print ("Name: " + player.name)
            print ("Wins: " + str(player.wincount))
            print ("Loss: " + str(player.losscount))
            print ("You have won " + str(round(player.winpercentage,2)) + "% of the games you have played.")
            print ("Most of your wins have come from " + player.winGameInfo.name + ", with " + str(player.winGameInfo.win) + " wins out of " + str(player.winGameInfo.count) + " games.")
            print ("Most of your loss have come from " + player.lossGameInfo.name + ", with " +  str(player.lossGameInfo.loss) + " loss out of " + str(player.lossGameInfo.count) + " games.")
            print ("Your h-index is: " + str(player.hIndex))
            #print "For every " + str(player.winratio) + " games you have won, you have lost 1 game."
            print ("Total Games Played: " + str(player.wincount + player.losscount))

    def _WinRatio(self):
        for player in self.playersInfo:
            if (player.wincount != 0) and (player.losscount != 0):
                player.winratio = float(player.wincount) / float(player.losscount)

    def _WinPercentage(self):
        for player in self.playersInfo:
            total = player.wincount + player.losscount
            percentage = 100 * float(player.wincount) / float(total)
            player.winpercentage = percentage
                                    
        
    

if __name__ == "__main__":
    main = BGGStats()
    main.Main()
