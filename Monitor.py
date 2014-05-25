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
import log
from WeiboInterface import WeiboInterface


import util

logger = log.getLogger("montior")

def cap_and_send_to_weibo():
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
        time.sleep(compute_loop_time())
        
    logger.info("finished, quit!")
    return 0

def cap_to_local_dir(dir='./', sleep_time=60):
    logger = log.getLogger("montior")
    logger.info("staring capture")
    cap = CapImage(0, dir)
    old_path = None
    while True:
        path = cap.getimage_path()
        if old_path == None:
            old_path = path
        try:
            logger.debug("cap image to [%s]" % path)
            # TODO need to compare with last image.
            # if they are same(means static image)
            # do not save the new captured image
            cap.capimage(path)
            print path
            print old_path
            print cap.imgcompare(old_path, path)
            if cap.imgcompare(old_path, path) > 0.97 and old_path != path:
                logger.debug("image is similar with old one, remove it")
                cap.remove_img(path)
            else:
                old_path = path
        except:
            logger.debug("cap image error [%s]" % path)
            old_path = None
        time.sleep(sleep_time)


if __name__ == '__main__':
	#
    #main()
    cap_to_local_dir(dir='/home/pi/images/',sleep_time=1)

