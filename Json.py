#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
json Api
'''
import json
import sys
import re
import weibo

class JsonProcessor:
	def Parse_json_2_list(self, ret):
		'''
		parse json to list
		'''
		textlist = []
		texts = _parse_json(ret)
		for text in texts:
			textlist.append(text)
		return textlist
	def Parse_get_text_from_json(self, texts, text='text'):
		'''
			get text content from a json string
		'''
		json_texts = weibo._parse_json(texts)
		return json_texts.get(text, False)
	def Parse_get_text_from_list(self, texts, text='text'):
		'''
			get text content from a list
		'''
		return texts.get(text, False)
	def Dump_json(self, key, value):
		print "Dump json"
		ret = json.dumps(['status','hello from shell'])
		return ret
		#return json.dump(key)
		
