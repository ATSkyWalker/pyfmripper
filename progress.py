#!/usr/bin/env python
# encoding: utf-8
"""
progress.py

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