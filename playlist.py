#!/usr/bin/env python
# encoding: utf-8
"""
playlist.py

Created by Ahmed Talaat on 2008-09-11.
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
import elementtree.ElementTree as ET
import urllib2
import pprint
from tagger import MP3Tagger
import time

class LastFMTrack:
	read_buffer_size = 1024 * 10 #10K chuncks
	def __init__(self, url, title, album, artist, duration, album_art_url):
		self.url 				= url
		self.title				= title
		self.name				= self.title
		self.album				= album
		self.artist				= artist
		self.duration			= duration
		self.album_art_url		= album_art_url
	
	def mystr(self):
		return [self.title, self.album, self.url, self.artist, self.duration]
	
	def rip(self, output_file_name, progress_hook):
		f = urllib2.urlopen(self.url)
		content_type = f.info()['Content-Type']
		length = f.info()['Content-Length']
		
		oFileName = output_file_name.strip()
		oFile = open(oFileName, 'wb')
		read_counter = 0
		while read_counter <= int(length):
			read_counter += LastFMTrack.read_buffer_size
			data = f.read(LastFMTrack.read_buffer_size)
			if progress_hook:
				progress_hook('%0.2f MB' %(read_counter/1024.0/1024.0))
			oFile.write(data)
		
		oFile.close()
		f.close()
			
		# tag the file
		tags = {}
		tags['title']  = self.title
		tags['album']  = self.album
		tags['artist'] = self.artist
		MP3Tagger.tagFile(oFileName, tags)
		
		
class LastFMPlayList:
	
	def __init__(self, url):
		self.version 	= None
		self.title		= None
		self.tracks		= []

		try:
			self.__parse__(url)
		except:
			# retry then fail
			time.sleep(5)
			self.__parse__(url)
			

		self.number_of_tracks = len(self.tracks)
	
	def __parse__(self, url):
		
		try:
			tree = ET.parse(urllib2.urlopen(url)).getroot()		
			self.version = tree.attrib['version']
			self.title = tree.find('title').text
		
			for ele in tree.findall('trackList/track'):
				track = LastFMTrack(ele.findtext('location'), 
									ele.findtext('title'),
									ele.findtext('album'),
									ele.findtext('creator'),
									ele.findtext('duration'),
									ele.findtext('image'))
								
				self.tracks.append(track)
		except urllib2.HTTPError, e:
			msg = "Error while getting Playlist: %d: %s" %(e.errno, e.message)
			print msg
			raise e
	
	def __str__ (self):
		return "Play List: %s - Version: %s" %(self.title, self.version)


