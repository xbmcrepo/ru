#!/usr/bin/python
# Copyright (c) 2011 XBMC-Russia, HD-lab Team, E-mail: dev@hd-lab.ru
# Writer (c) 2011, Kostynoy S.A., E-mail: seppius2@gmail.com

import sys, os, xbmcaddon

__addon__ = xbmcaddon.Addon( id = 'plugin.video.xbmc.rus' )
sys.path.append( os.path.join( __addon__.getAddonInfo( 'path' ), 'resources', 'lib') )

if (__name__ == '__main__' ):
	import xbmcrussia
	xbmcrussia.addon_main()
