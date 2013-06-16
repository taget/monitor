#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  logger.py
#  
#  Copyright 2013 lenovo <lenovo@N-QIAOLIYONG>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import logging

class logger:
	def __init__(self, file):
		
		self.log_file = file
		
		formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
		handler = logging.FileHandler(self.log_file)
		handler.setFormatter(formatter)
		self.logger = logging.getLogger()
		self.logger.setLevel(logging.NOTSET)
		self.logger.addHandler(handler)
	
	def info(self, msg):
		self.logger.info(msg)
		
	def error(self, msg):
		self.logger.error(msg)
