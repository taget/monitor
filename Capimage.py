#!/usr/bin/env python
# -*- coding: utf-8 -*-

#sudo apt-get install python-opencv
import cv
import os, time
import log
import util

class CapImage:
	
    def __init__(self, device = 0, save_dir = "./"):
        self.log_file = "capimges.log"

        self._logger = log.getLogger(self.log_file)
		
        self._saved_dir = save_dir if save_dir else "./"
        self._saved_path = ""
		
        self._cap = cv.CaptureFromCAM(0)
        cv.SetCaptureProperty(self._cap, cv.CV_CAP_PROP_FRAME_HEIGHT, \
                                      240)
        cv.SetCaptureProperty(self._cap, cv.CV_CAP_PROP_FRAME_WIDTH, \
                                      320)

	
    def capimage(self, path = None):
        '''
        save a image to path
        '''
        path = path if not path == None else self.getimage_path()
        frame = cv.QueryFrame(self._cap)
        if not frame == None:
            cv.SaveImage(path, frame)
            return path
        else:
            self._logger.error("Capture image error!")
            return None

		
    def getimage_path(self):
        path = ".jpg"
        path = util.get_systime() + path
        self._saved_path = self._saved_dir + path
        return self._saved_path

    def _createHist(self, img):
        b_plane = cv.CreateImage((img.width,img.height), 8, 1)
        g_plane = cv.CreateImage((img.width,img.height), 8, 1)
        r_plane = cv.CreateImage((img.width,img.height), 8, 1)

        cv.Split(img,b_plane,g_plane,r_plane,None)
        planes = [b_plane, g_plane, r_plane]
    
        bins = 4
        b_bins = bins
        g_bins = bins
        r_bins = bins

        hist_size = [b_bins,g_bins,r_bins]
        b_range = [0,255]
        g_range = [0,255]
        r_range = [0,255]

        ranges = [b_range,g_range,r_range]
        hist = cv.CreateHist(hist_size, cv.CV_HIST_ARRAY, ranges, 1)
        cv.CalcHist([cv.GetImage(i) for i in planes], hist)
        cv.NormalizeHist(hist,1)
        return hist

# return a double [0-1]
# if > 0.95 , which mean the two images are similar
    def imgcompare(self, image1,image2):
        img1 = cv.LoadImage(image1)
        hist1 = self._createHist(img1)
        img2 = cv.LoadImage(image2)
        hist2 = self._createHist(img2)
        return cv.CompareHist(hist1, hist2, cv.CV_COMP_CORREL)

def test():
    cap = CapImage()
    print cap.imgcompare("/home/pi/code/1.jpg","/home/pi/code/4.jpg")
    
def main():
    cap = CapImage()
    cap.capimage()
    return 0

if __name__ == '__main__':
    test()
    #main()

