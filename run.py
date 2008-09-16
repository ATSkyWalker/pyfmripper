#!/usr/bin/env python
# encoding: utf-8
"""
run.py

Copyright (c) 2008 Ahmed Talaat.


This file is part of PyFMRipper.

PyFMRipper is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PyFMRipper is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PyFMRipper.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys
import os
import lastfm
import urllib2
from progress import TwirlyBar
from playlist import LastFMTrack

from optparse import OptionParser

	
tb = TwirlyBar()

def main():

	parser = OptionParser()	

	parser.add_option("-u", "--user_name",
	                  action="store", dest="user_name",
	                  help="Last.fm username")

	parser.add_option("-p", "--password",
	                  action="store", dest="password",
	                  help="Last.fm password")

	parser.add_option("-c", "--channel",
	                  action="store", dest="channel",
	                  help="Last.fm artist channel")
	
	
	parser.add_option("-d", "--destination",
					  action="store", dest="dest", default="./",
					  help="file store destination")
	
	
	(options, args) = parser.parse_args()
	
	if options.user_name == None or options.password == None or options.channel == None:
		parser.print_help()
		exit(-1)

	session = lastfm.LastFMSession()
	session.handshake(options.user_name, options.password)
	

	session.set_artist(options.channel)
	for x in range(1,10):
		play_list = session.get_play_list()
		ripTracks(play_list, options.dest)
	
	print "All Done...."

def ripTracks(play_list, dest):
	
	for track in play_list.tracks:
		output_file_name = os.path.join(dest, track.name) + ".mp3     "
		sys.stdout.write("\ndownloading file: " + output_file_name)
		sys.stdout.flush()
		track.rip(output_file_name, tb.ShowProgress)
		tb.reset()
	
def test():
	pass

if __name__ == '__main__':
	main()
	#test()

