#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  WeiboInterface.py
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
app_key = '35587412'
app_secret = '1b054a023d36fbacd3e26a5b723baf4d'
r_url = 'https://api.weibo.com/oauth2/default.html'

import time,os,sys
from logger import logger
from Readcode import ReadCode

logger = logger("main.log")

from weibo import APIClient
from message_list import message_list

def format_msg(*arg):
        for x in arg:
                print x,
        print ''

class WeiboInterface:
	
	def __init__(self):
		self._client = APIClient(app_key, app_secret, r_url)
		url = self._client.get_authorize_url()
		print url
		print "please echo \$code > code.data in another shell"
		rd = ReadCode()
		code = rd.get_code()
		# todo need to check code
		print code
		r = self._client.request_access_token(code)
		self._client.set_access_token(r.access_token, r.expires_in)
	
	def get_msg(self):
		#msg = self._client.statuses__friends_timeline()
		#print msg
		msg = self._client.statuses.user_timeline.get()
		#return 1
		msg_list = message_list(msg)

		i = 0
		while i < msg_list.get_msg_count():
			msg = msg_list.get_message(i)
			usr = msg.msg_user()
			retweeted_msg = msg.msg_retweeted_status()
			if retweeted_msg == None:
				format_msg(i, ':[',usr.get_user_name(),\
                                ']:[', msg.msg_text(), ']')
			else:
				re_usr = retweeted_msg.msg_user()
				format_msg(i,':[',usr.get_user_name(),\
                                ']:[', msg.msg_text(),']')
				format_msg('----origin message:---- \
                                [', re_usr.get_user_name(), ']:[',\
                                retweeted_msg.msg_text(),']')
			i = i + 1
	def uploade_img(self, file_path):
		self._ret_msg = self._client.upload.statuses__upload( \
		             status='uploaded at ' + str(time.time()),\
		             pic=open(file_path, 'rb'))
		return self.parse_msg()
	
	def parse_msg(self):
		'''
		TODO
		'''
		print self._ret_msg
		return True


