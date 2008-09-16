#!/usr/bin/env python
# encoding: utf-8
"""
lastfmTests.py

Created by Ahmed Talaat on 2008-09-15.
Copyright (c) 2008 Spade Consulting Inc.. All rights reserved.
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
