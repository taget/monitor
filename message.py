#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
return message
'''
from user import user

class message:
	def __init__(self, msg):
		self._msg = msg
		# user 
		self._user = user(self._msg.get('user'))
		
		# 
		self._created_at = self._msg.get('created_at')
		self._id = self._msg.get('id')
		self._text = self._msg.get('text')
		
	def created_time(self):
		return self._created_at
		
	def msg_id(self):
		return self._id
		
	def msg_text(self):
		return self._text
		
	def msg_user(self):
		return self._user
		
# if retweeted_status is none
	def msg_retweeted_status(self):
		try:
			 tmp = self._msg.get('retweeted_status')
			 return message(tmp)
		except:	 
			 return None

		
