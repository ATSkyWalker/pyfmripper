#!/usr/bin/env python
# encoding: utf-8
"""
tagger.py

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
# from mutagen.mp3 import MP3
# from mutagen.id3 import ID3
# from mutagen.id3 import TextFrame
# from mutagen.id3 import TIT2
# from mutagen.easyid3 import EasyID3
import eyeD3

class MakeStaticCallable:
    def __init__(self, anycallable):
        self.__call__ = anycallable

class MP3Tagger:
	def __init__(self):
		pass
	
	def tagFile(file_name, tags):

		tag = eyeD3.Tag()
		tag.link(file_name)    # no tag in this file, link returned False
		tag.header.setVersion(eyeD3.ID3_V2_3)
		tag.setArtist(tags['artist'])
		tag.setAlbum(tags['album'])
		tag.setTitle(tags['title'])
		tag.update()
		
	
	#Make the only method in this class static
	tagFile = MakeStaticCallable(tagFile)



if __name__ == '__main__':
	tags = {}
	tags['title'] = 'This is the title'
	tags['album'] = 'This is the album'
	tags['artist'] = 'This is the artist'
	MP3Tagger.tagFile("./mp3s/Signs of Life.mp3",tags)