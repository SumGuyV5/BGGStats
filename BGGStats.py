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
import operator
import BGGModule.Functions

from BGGModule.ReadXML import ReadXML
from BGGModule.DownloadXML import DownloadXML


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

        self.players_info = []
        
        self.downloadXML = DownloadXML(self.url, self.filename)
        self.readXML = ReadXML()
        self.re_download = True

    def main(self):
        count_to = BGGModule.Functions.count_to(self.username, self.pagesize)
        if self.re_download:
            self.downloadXML.download_all(self.url, "plays", count_to)
        self.readXML.read_xml_all(os.path.join(os.getcwd(), "plays"), count_to)
            
        self.players_info = BGGModule.Functions.load_info(self.ignore, self.readXML.plays)
        self.players_info = sorted(self.players_info, key=operator.attrgetter('win_percentage'), reverse=True)
        self.print_stats()

    def download(self, number):
        self.downloadXML.url = self.url + str(number)
        self.downloadXML.download()

    def print_stats(self):
        for player in self.players_info:
            if player.name in self.ignore:
                continue
            print("\n")
            print(f'Name: {player.name}')
            print(f'Wins: {str(player.win_count)}')
            print(f'Loss: {str(player.loss_count)}')
            print(f'You have won {str(round(player.win_percentage, 2))}% of the games you have played.')
            print(f'Most of your wins have come from {player.win_info.name}, with {str(player.win_info.win)} '
                  f'wins out of {str(player.win_info.count)} games.')
            print(f'Most of your loss have come from {player.loss_info.name}, with {str(player.loss_info.loss)} '
                  f'loss out of {str(player.loss_info.count)} games.')
            print(f'Your h-index is: {str(player.h_index)}')
            # print(f'For every 1 games you have won, you have lost {str(player.winratio)} game.')
            print(f'Total Games Played: {str(player.win_count + player.loss_count)}')
            print(f'You have: {str(player.points)} points.')
            print(f'You get: {str(player.points_per_game)} points per game.')


if __name__ == "__main__":
    main = BGGStats()
    main.main()
