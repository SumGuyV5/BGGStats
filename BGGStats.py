#!/usr/bin/env python
"""***************************************************************
**  Program Name:   BGGStatus				        **
**  Version Number: V0.6                                        **
**  Copyright (C):  September 3, 2014 Richard W. Allen          **
**  Date Started:   September 18, 2019                           **
**  Date Ended:     May 15, 2019                                **
**  Author:         Richard W. Allen                           **
**  Webpage:        http://www.richardallenonline.com           **
**  IDE:            IDLE 3.6.5                                  **
**  Compiler:       Python 3.6.5                                **
**  Language:        Python 3.6.5				**
**  License:	    GNU GENERAL PUBLIC LICENSE Version 2	**
**		    see license.txt for for details	        **
***************************************************************"""
import os
import BGGModule.Functions

from BGGModule.PlayerInfo import PlayerInfo
from BGGModule.ReadXML import ReadXML
from BGGModule.DownloadXML import DownloadXML
from BGGModule.GameInfo import GameInfo


class BGGStats:
    def __init__(self):
        self.pagesize = 100
        self.username = "SumGuyV5"

        self.ignore = ['Keith', 'Paul', 'Dempsey', 'Other', 'Kelly', 'Alyssa', 'Player 6', 'Mark', 'Player 7',
                       'Beulah', 'Besa', 'Player 5', 'Raymon', 'Play 2', 'Jay', 'Play 6', 'Play 5', 'Play 4', 'Play 3',
                       'Anthony', 'Bill']
        
        self.url = f'http://www.boardgamegeek.com/xmlapi2/plays?username={self.username}' \
            f'&pagesize={str(self.pagesize)}&page='
        self.filename = "plays.xml"

        self.playersInfo = []
        
        self.downloadXML = DownloadXML(self.url, self.filename)
        self.readXML = ReadXML()
        self.re_download = True

    def main(self):
        count_to = BGGModule.Functions.play_count(self.username, self.pagesize)
        if self.re_download:
            self.downloadXML.download_all(self.url, "plays", count_to)
        self.readXML.read_xml_all(os.path.join(os.getcwd(), "plays"), count_to)
            
        self.load_info()
        self.sort_players("winpercentage")
        self.print_stats()

    def load_info(self):
        for play in self.readXML.plays:
            if (play.incomplete == 0) and (play.nowinstate == 0):
                for player in play.players:
                    if self.add_player(player.username, player.name, player.win, play.gamename) is False:
                        print("Error Player not found!")

    def add_player(self, username, name, win, gamename):
        found = False
        for playerInfo in self.playersInfo:
            if (playerInfo.username == username) and (playerInfo.name == name):
                found = True
                self.add_game_info(gamename, win, playerInfo)
                if win is True:
                    playerInfo.wincount += 1
                else:
                    playerInfo.losscount += 1
        if found is False:
            self.playersInfo.append(PlayerInfo(name, username))
            found = self.add_player(username, name, win, gamename)

        return found

    def add_game_info(self, name, win, playerinfo):
        found = False
        for game_info in playerinfo.gameinfo:
            if game_info.name == name:
                found = True
                game_info.add_count(win)
        if found is False:
            playerinfo.gameinfo.append(GameInfo(name))
            found = self.add_game_info(name, win, playerinfo)
        return found

    def download(self, number):
        self.downloadXML.url = self.url + str(number)
        self.downloadXML.download()

    def sort_players(self, sortby):
        for player in self.playersInfo:
            player.load_game_info()
        if sortby == "wincount":
            self.playersInfo = sorted(self.playersInfo, key=lambda playersinfo: playersinfo.wincount, reverse=True)
        elif sortby == "winpercentage":
            self.playersInfo = sorted(self.playersInfo, key=lambda playersinfo: playersinfo.winpercentage, reverse=True)

    def print_stats(self):
        for player in self.playersInfo:
            if player.name in self.ignore:
                continue
            print("\n")
            print(f'Name: {player.name}')
            print(f'Wins: {str(player.wincount)}')
            print(f'Loss: {str(player.losscount)}')
            print(f'You have won {str(round(player.winpercentage,2))}% of the games you have played.')
            print(f'Most of your wins have come from {player.winGameInfo.name}, with {str(player.winGameInfo.win)} '
                  f'wins out of {str(player.winGameInfo.count)} games.')
            print(f'Most of your loss have come from {player.lossGameInfo.name}, with {str(player.lossGameInfo.loss)} '
                  f'loss out of {str(player.lossGameInfo.count)} games.')
            print(f'Your h-index is: {str(player.hIndex)}')
            # print(f'For every 1 games you have won, you have lost {str(player.winratio)} game.')
            print(f'Total Games Played: {str(player.wincount + player.losscount)}')


if __name__ == "__main__":
    main = BGGStats()
    main.main()
