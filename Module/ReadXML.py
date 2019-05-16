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
import sys
sys.path.append('Module.zip')

from Module.PlaysDataset import PlaysDataset
from Module.PlayerDataset import PlayerDataset

from xml.dom.minidom import parse, getDOMImplementation

class ReadXML:
    def __init__(self):
        self._dom = object

        self.playcount = 0

        self.plays = []

    def ReadXMLFile(self, filename):
        try:
            self._dom = parse(filename)
        except:
            print ('File IO Error on file name ' + filename)

        plays_info = self._dom.getElementsByTagName("plays")
        for play_info in plays_info:
            self.playcount = int(play_info.attributes['total'].value)

        plays = self._dom.getElementsByTagName("play")
        for play in plays:
            playsDataset = self._ReadXMLPlays(play)
            self._ReadXMLPlayers(play, playsDataset)
            self.plays.append(playsDataset)
                
    def _ReadXMLPlays(self, dom):
        rtn = PlaysDataset()
        rtn.length = int(dom.attributes['length'].value)
        rtn.location = dom.attributes['location'].value
        rtn.incomplete = int(dom.attributes['incomplete'].value)
        rtn.nowinstate = int(dom.attributes['nowinstats'].value)
        rtn.date(dom.attributes['date'].value)
        items = dom.getElementsByTagName("item")
        for item in items:
            rtn.gamename = item.attributes['name'].value
        
        return rtn
                
    def _ReadXMLPlayers(self, dom, playsDataset):       
        players = dom.getElementsByTagName("player")
        for player in players:
            playsDataset.AddPlayer(self._LoadPlayers(player))

    def _LoadPlayers(self, player):
        rtn = PlayerDataset()
        rtn.username = player.attributes['username'].value
        rtn.name = player.attributes['name'].value
        rtn.colour = player.attributes['color'].value
        rtn.win = bool(int(player.attributes['win'].value))
        rtn.new = bool(int(player.attributes['new'].value))

        return rtn


if __name__ == "__main__":

    print ("Testing... ReadXML Class")
    read = ReadXML()

    read.ReadXMLFile(os.getcwd() + '\\..\\plays.xml')

    for play in read.plays:
        print ("Name: " + play.gamename)
        """ #print "Username: " + player.username
        print "Name: " + player.name
        print "Wins: " + str(player.wincount)
        print "Loss: " + str(player.losscount)
        print "Total Games Played: " + str(player.wincount + player.losscount)
        print """
        
