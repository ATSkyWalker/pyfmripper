#!/usr/bin/env python
# encoding: utf-8
"""
lastfm.py

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
import urllib2
import urllib
import hashlib
import re
from playlist import LastFMPlayList

class LastFMSession:
	def __init__(self):
		self.session_id 		= None
		self.stream_url			= None
		self.base_url			= None
		self.base_path			= None
		self.login_error_msg 	= None


	def _response_to_dict(self, response):
		p = re.compile('(.+?)=(.+)', re.M)
		it = p.finditer(response)
		result = {}
		for m in it:
			result[m.group(1)] = m.group(2)
		return result

	def handshake(self, username, password):
		md5 = hashlib.md5()
		md5.update(password)
		hashed_password = md5.hexdigest()
		params = {
					'version' 		: '1.3.1.1',
				 	'platform'		: 'mac',
					'username'		: username,
					'passwordmd5'	: hashed_password,
					'language'		: 'en'
				 }
		encoded_params = urllib.urlencode(params)
		try:
			f = urllib2.urlopen("http://ws.audioscrobbler.com/radio/handshake.php?%s" %encoded_params)
			response =  f.read()

			response_dict = self._response_to_dict(response)
			# print response_dict
			self.session_id = response_dict['session']
			
			if self.session_id == "FAILED":
				self.login_error_msg = response_dict['msg']
				return False
			
			self.stream_url = response_dict['stream_url']
			self.base_url	= response_dict['base_url']
			self.base_path	= response_dict['base_path']
			return True
			
		except urllib2.HTTPError, e:
			msg = "HTTP Error: %d%s" %(e.code,"\n")
			sys.stderr.write(msg)
			self.login_error_msg = msg
			return False
		
		
	def set_artist(self, artist_name):
		artist_path = 'lastfm://artist/' + urllib.quote_plus(artist_name) + '/similarartists'
		url = "http://" + self.base_url + self.base_path + "/adjust.php?session=%s&url=%s&lang=%s" % (self.session_id, artist_path, 'en')
		
		f = urllib2.urlopen(url)
		result = f.read()
		if self._response_to_dict(result)['response'] != "OK":
			return False
		else:
			return True
	
	def get_play_list(self):
		url = url = "http://" + self.base_url + self.base_path + "/xspf.php?sk=" + self.session_id + "&discovery=0&desktop=1.3.1.1"
		play_list = LastFMPlayList(url)
		return play_list























