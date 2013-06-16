#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
user
'''

class user:
	def __init__(self, msg):
		self._msg = msg
		self._user_name = msg.get('name')
		
	def get_user_name(self):
		return self._user_name
