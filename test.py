#!/usr/bin/env /usr/bin/python
# -*- coding: utf-8 -*-
#
#  test.py
#  

import sys
import os
import time
from logger import logger
from WeiboInterface import WeiboInterface
from Capimage import CapImage

logger = logger("test.log")

max_loop = 100
sleep_time = 100


def compute_loop_time():
	return sleep_time


def testCapImage():
	# capiture device 1 [we have 0,1]
        capimg = CapImage()
        capimg.capimage()

def testweibo():
	web = WeiboInterface()
	web.get_msg()

def main():
	testweibo()

if __name__ == '__main__':
	main()

