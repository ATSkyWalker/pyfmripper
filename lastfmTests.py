#!/usr/bin/env python
# encoding: utf-8
"""
lastfmTests.py

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
import unittest
from lastfm import LastFMSession
from playlist import LastFMTrack,LastFMTrack


class TestModule(unittest.TestCase):
	def setUp(self):
		self.username 		= '' # put your username here if you want to test.
		self.password 		= '' # Put your password here if you want to run the tests!
		self.bad_password	= 'some_password'
		self.session = LastFMSession()
		
	def testHandshakeWithGoodCredentials(self):
		result = self.session.handshake(self.username, self.password)
		self.assertEqual(result, True)
	def testHandshakeWithBadCredentials(self):
		result = self.session.handshake(self.username, self.bad_password)
		self.assertEqual(result, False)
	def testArtistFlipChannel(self):
		result = self.session.handshake(self.username, self.password)
		self.assertEqual(result, True)
		
		result = self.session.set_artist("Jack Johnson")		
		self.assertEqual(result, True)
	
		result = self.session.set_artist("dskjhdfjksdfhuriuyr")		
		self.assertEqual(result, False)
	
	def testGettingPlayList(self):
		result = self.session.handshake(self.username, self.password)
		self.assertEqual(result, True)

		result = self.session.set_artist("Jack Johnson")		
		self.assertEqual(result, True)
		
		result = self.session.get_play_list()
		self.assertEqual(result.version, '1')
		self.failUnless(len(result.tracks) > 1)

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestModule)
	unittest.TextTestRunner(verbosity = 2).run(suite)
