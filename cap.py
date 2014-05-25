import sys
import os
import time
from logger import logger
from WeiboInterface import WeiboInterface
import cv

cap = cv.CaptureFromCAM(0)
cv.SetCaptureProperty(cap, cv.CV_CAP_PROP_FRAME_HEIGHT, 240)
cv.SetCaptureProperty(cap, cv.CV_CAP_PROP_FRAME_WIDTH, 320)


def cap_img(file):
	frame = cv.QueryFrame(cap)
 	cv.SaveImage(file, frame)
	return file

def remove_img(file):
	if os.path.exists(file):
		os.remove(file)
		return True
	else:
		return False
	
logger = logger("main.log")

def test():
	img_file = 'tmp.jpg'
	path = cap_img(img_file)

def main():
	img_file = 'tmp.jpg'
        weibo = WeiboInterface()
	path = cap_img(img_file)
        weibo.uploade_img(path)
	remove_img(path)

if __name__ == '__main__':
    test()    
	#main()
