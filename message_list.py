#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
return message_list
1 message_list contain some messages
'''
from Json import JsonProcessor
from message import message
class message_list:
	def __init__(self, msg):
		self._msg = msg
		self._jsonprocessor = JsonProcessor()
		self._statuses = self._jsonprocessor.Parse_get_text_from_json(self._msg, 'statuses')
		self._len = len(self._statuses)
		self._msg_list = []
		i = 0
		while i < self._len:
			self._msg_list.append(message(self._statuses[i]))
			i = i + 1
# message list body	
	def get_statuses(self):
		return self._statuses
# message length
	def get_msg_count(self):
		return self._len
# message text[i]
	def get_status_of_i(self, i):
		return self._statuses[i]
# return message[i]
	def get_message(self, i):
		return self._msg_list[i]
		
	
