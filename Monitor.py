#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Monitor.py
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

from Capimage import CapImage
import sys
import os
import time
from logger import logger
from WeiboInterface import WeiboInterface

logger = logger("main.log")

max_loop = 100
sleep_time = 100


def compute_loop_time():
	return sleep_time

def main():
	# capiture device 1 [we have 0,1]
	cap = CapImage(0)
	weibo = WeiboInterface()

	looper = 0

	while looper < max_loop:
		looper = looper + 1

		path = cap.getimage_path()
		try:
			cap.capimage(path)
			logger.info(path)
		except:
			logger.info('error to cap a image')
			continue

		try:
			weibo.uploade_img(path)
			logger.info("send to weibo")
		except:
			logger.info("send error!")
		cap.remove_img()
		time.sleep(sleep_time)
        
	logger.info("finished, quit!")
	return 0

if __name__ == '__main__':
	main()

