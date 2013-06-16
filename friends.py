#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
show friends
'''
from Interface import WeiboInterface
from message_list import message_list

def format_msg(*arg):
	for x in arg:
		print x,
	print ''
		
class friends:
	def __init__(self, interface, cmdline):
		self._command_line = cmdline
		self._interface = interface
	def run(self):
		print '查看最新...'
		self._interface.seturl(self._command_line)
		self._interface.addopt('count','2')
		ret = self._interface.callweibo()
		msg_list = message_list(ret)
		
		i = 0
		while i < msg_list.get_msg_count():
			msg = msg_list.get_message(i)
			usr = msg.msg_user()
			retweeted_msg = msg.msg_retweeted_status()
			if retweeted_msg == None:
				format_msg(i, ':[',usr.get_user_name(), ']:[', msg.msg_text(), ']')
			else:
				re_usr = retweeted_msg.msg_user()
				format_msg(i,':[',usr.get_user_name(), ']:[', msg.msg_text(),']')
				format_msg('----原文转发---- [', re_usr.get_user_name(), ']:[', retweeted_msg.msg_text(),']')
			i = i + 1

