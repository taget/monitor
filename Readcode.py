#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, time
from logger import logger

class ReadCode:
	def __init__(self, codefile = 'code.data'):
		self._file = codefile
		self._code = ""
	def get_code(self):
		while True:
			try:
				with open(self._file) as codefile:
					for line in codefile:
						self._code = line.strip('\n')
						
				os.remove(self._file)
				return self._code
			except:
				time.sleep(1)
	
