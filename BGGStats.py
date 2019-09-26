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

        self.players_info = []
        
        self.downloadXML = DownloadXML(self.url, self.filename)
        self.readXML = ReadXML()
        self.re_download = False

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
            if (play.incomplete == 0) and (play.now_in_state == 0):
                players_points = play.points()
                for player in play.players:
                    if self.add_player(player.username, player.name, player.win, play.game_name, players_points[player.name]) is False:
                        print("Error Player not found!")

    def add_player(self, username, name, win, game_name, points):
        found = False
        for player_info in self.players_info:
            if (player_info.username == username) and (player_info.name == name):
                found = True
                self.add_game_info(game_name, win, player_info)
                if win is True:
                    player_info.win_count += 1
                else:
                    player_info.loss_count += 1
                player_info.points += points
        if found is False:
            self.players_info.append(PlayerInfo(name, username))
            found = self.add_player(username, name, win, game_name, points)

        return found

    def add_game_info(self, name, win, player_info):
        found = False
        for game_info in player_info.games_info:
            if game_info.name == name:
                found = True
                game_info.add_count(win)
        if found is False:
            player_info.games_info.append(GameInfo(name))
            found = self.add_game_info(name, win, player_info)
        return found

    def download(self, number):
        self.downloadXML.url = self.url + str(number)
        self.downloadXML.download()

    def sort_players(self, sort_by):
        if sort_by == "wincount":
            self.players_info = sorted(self.players_info, key=lambda players_info: players_info.wincount, reverse=True)
        elif sort_by == "winpercentage":
            self.players_info = sorted(self.players_info, key=lambda players_info: players_info.win_percentage,
                                       reverse=True)

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
