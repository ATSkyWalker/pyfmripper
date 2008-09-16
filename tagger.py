#!/usr/bin/env python
# encoding: utf-8
"""
tagger.py

Created by Ahmed Talaat on 2008-09-13.
Copyright (c) 2008 Spade Consulting Inc.. All rights reserved.
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