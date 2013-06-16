#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv
import os, time
from logger import logger

class CapImage:
	
	def __init__(self, device = 0, save_dir = "./"):
		self.log_file = "capimges.log"

		self._logger = logger(self.log_file)
		
		self._logger.info("Capimage starting...")
		self._sleep_time = 1
		self._loop = True
		self._saved_dir = save_dir if save_dir else "./"
		self._saved_path = ""
		
		self._max_loop = 50

		self._cap = cv.CaptureFromCAM(0)
		cv.SetCaptureProperty(self._cap, cv.CV_CAP_PROP_FRAME_HEIGHT, \
                                      240)
		cv.SetCaptureProperty(self._cap, cv.CV_CAP_PROP_FRAME_WIDTH, \
                                      320)

	
	def capimage(self, path = None):
		'''
		save a image to path
		'''
		print path
		path = path if not path == None else self.getimage_path()
		frame = cv.QueryFrame(self._cap)
        	if not frame == None:
			cv.SaveImage(path, frame)
			self._logger.info("Image saved to %s" % path)
		else:
			self._logger.error("Capture image error!")

		
	def getsystime(self):
		return str(time.time())
		
	def getimage_path(self):
		path = ".jpg"
		path = self.getsystime() + path
		self._saved_path = self._saved_dir + path
		return self._saved_path
	
	def remove_img(self):
		if os.path.exists(self._saved_path):
			os.remove(self._saved_path)
			self._saved_path = ""
			return True
		else:
			return False
	
	def start(self):
		self._logger.info("New loop")
		looper = 1
		while self._loop and looper < self._max_loop:
			path = self.getimage_path()
			self.capimage(path)
			time.sleep(self._sleep_time)
			
	
def main():
	cap = CapImage()
	cap.start()
	return 0

if __name__ == '__main__':
	main()

