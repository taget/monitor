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
import threading

import log
from WeiboInterface import WeiboInterface


import util

logger = log.getLogger("montior")
threadLock = threading.Lock()

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

def cap_to_local_dir(cap):
    path = cap.getimage_path()
    try:
        cap.capimage(path)
    except:
        logger.error("cap image error [%s]" % path)
        return None
    return path

# check the dir size every sleep_time
# 
# 20 * 1024 *1024
def archive_to_tgz (srcdir='./', destdir= '/home/pi/', fold_size = 3 * 1024 *1024):
    
    size = util.get_FolderSize(srcdir)
    failed = 0
    if size > fold_size:
        # need to archive
        tgz_name = destdir + '/' + util.get_systime() + '.tgz'
        try:
            util.zip_dir(srcdir, tgz_name)
        except util.UtilException as e:
            print e.msg
            failed = 1
        if not failed == 1:
            util.remove_files(srcdir)
            return tgz_name
        else:
            return None
    else:
        return None
        
    
# todo
# start 2 thread
# 1 for capture images to some where
# 2 for check the file size and archive them
#dirname
#sleep_time
class cap_Thread(threading.Thread):
    def __init__(self, dirname , sleep_time=1):
        threading.Thread.__init__(self)
        self.dirname = dirname
        self.sleep_time = sleep_time
        self.cap = CapImage(0, dirname)
        
    def run(self):
        print "Starting capture" + self.dirname
        old_path = None
        while True:
            threadLock.acquire()
            path = cap_to_local_dir(self.cap)
            if not path == None:
                if old_path == None:
                    old_path = path
                if self.cap.imgcompare(old_path, path) > 0.97 and \
                   not old_path == path:
                    logger.debug("image is similar with old one, remove it")
                    util.remove_file(path)
                else:
                    logger.debug("image saved to %s" % path)
                    old_path =  path
            else:
                logger.error("capture image error!")
                old_path = None
            threadLock.release()
            time.sleep(self.sleep_time)

#srcname
#destname
#size
#sleep_time
class archive_Trhead(threading.Thread):
    def __init__(self, srcname, destname, size, sleep_time=100):
        threading.Thread.__init__(self)
        self.srcname = srcname
        self.destdir = destname
        self.size = size
        self.sleep_time = sleep_time
        
    def run(self):
         print "Starting Archive service... " + self.srcname
         while True:
            threadLock.acquire()
            filename = archive_to_tgz(self.srcname, self.destdir, self.size)
            if not filename == None:
                logger.info("Archive to %s", filename)
            threadLock.release()
            time.sleep(self.sleep_time)
         
def test():
    thread_cap = cap_Thread("/home/pi/images/", 2)
    thread_archive = archive_Trhead("/home/pi/images/", '/home/pi/', 3*1024*1024,\
                    sleep_time = 10*60)
    thread_cap.start()
    thread_archive.start()
    
    thread_cap.join()  
    thread_archive.join()
    print "Exiting Main Thread"

if __name__ == '__main__':
	#
    #main()
    #cap_to_local_dir(dir='/home/pi/images/',sleep_time=1)
    test()

