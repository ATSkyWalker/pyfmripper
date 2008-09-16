#!/usr/bin/env python
# encoding: utf-8
"""
progress.py

Created by Ahmed Talaat on 2008-09-12.
Copyright (c) 2008 Spade Consulting Inc.. All rights reserved.
"""

import sys
import os



class TwirlyBar:
	def __init__(self):
		import sys
		self.__state = 0
		self.__bar = ('|', '/', '-', '\\')
		self.__initialized = False
		
	def ShowProgress(self, extra_info):
		if (self.__initialized):
			output = ('\b' * (7 + len(extra_info))) + ('[ ' + self.__bar[self.__state] + '  ' + extra_info +' ]') 
		else:
			output = '[ ' + self.__bar[self.__state] + extra_info +' ]'
			self.__initialized = True
		
		sys.stdout.write(output)
		sys.stdout.flush()
		self.__state = self.__state + 1
		if self.__state > 3: self.__state = 0
	
	def reset(self):
		self.__initialized = False



if __name__ == "__main__":
    import sys, time
    sys.stdout.write ("Processing ...  ")
    tb = TwirlyBar()
    for x in range(10):
        tb.ShowProgress(None)
        time.sleep(0.5)
    sys.stdout.write("\bdone\n")