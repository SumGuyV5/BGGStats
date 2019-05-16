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
from urllib.request import urlretrieve

class DownloadXML:
    def __init__(self, url, filename):
        """init the variables"""
        self.url = url
        self.filename = filename

    def Download(self):
        print ("Download Starting!")
        print (self.url)
        urlretrieve(self.url, self.filename)
        print ("Download Complete!")

if __name__ == "__main__":
    print ("Testing... DownloadXML Class")
    url = "http://www.boardgamegeek.com/xmlapi2/plays?username=SumGuyV5"
    download = DownloadXML(url)
    download.Download()
