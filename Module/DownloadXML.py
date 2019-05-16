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

import urllib

class DownloadXML:
    def __init__(self, url, filename):
        """init the variables"""
        self.url = url
        self.filename = filename

    def Download(self):
        print "Download Starting!"
        print self.url
        urllib.urlretrieve(self.url, self.filename)
        print "Download Complete!"

if __name__ == "__main__":

    print "Testing... DownloadXML Class"
    url = "http://www.boardgamegeek.com/xmlapi2/plays?username=SumGuyV5"
    download = DownloadXML(url)
    download.Download()
