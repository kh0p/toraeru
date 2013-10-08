#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
	*booru general file.
	For now, there's working Gelbooru downloader for loli content,
	but soon I'll add danbooru, etc.
"""

import loli_spam
import os
import datetime
import urllib.request
import http.cookiejar
import xml.etree.ElementTree as eltree
import json


loli_spam.execute_spam()
cache_dir = "cache/"

class Gelbooru(object):
	"""docstring for Gelbooru"""
	
	def __init__(self, url="http://gelbooru.com/"):
		# gets gelbooru homepage by default
		super(Gelbooru, self).__init__() 
		self.url = url

		gelbooru_loli = urllib.request.urlopen(url,timeout=5)
		read_gel_loli = gelbooru_loli.read()

		# save to gel.html file
		name_gel_loli = "gel.html"
		file_gel_loli = open(cache_dir+name_gel_loli,"wb")
		file_gel_loli.write(read_gel_loli)
	
	def gel_rssatom(url="http://gelbooru.com/index.php?page=atom", 
					by_tag_loli = False,limit = 100,download = True):
		"""gel_rssatom:

		by_tag_loli: 
			If you want to get feed for tag 'loli', you need to switch 
			by_tag_loli to True.
		limit: 
			limit is variable that stores maximum number of loli entries. 
			maximum number of entries that can be loaded is 100 (limited 
			by gelbooru API). When I was testing it, there was some problem
			with loading less than 5-10 urls.
		"""

		if by_tag_loli == True:
			url = "http://gelbooru.com/index.php?page=dapi&s=post&q=index&limit={0}&tags=loli".format(str(limit))

		# gets gelbooru atom rss feed	
		gelbooru_atom = urllib.request.urlopen(url,timeout=5)
		read_gel_atom = gelbooru_atom.read()

		# save to atom.xml file
		if by_tag_loli == True:
			name_gel_atom = "atom_loli.xml"
		else: name_gel_atom = "atom.xml"
		file_gel_atom = open(cache_dir+name_gel_atom,"wb")
		file_gel_atom.write(read_gel_atom)

		# XML parsing 
		tree = eltree.parse(cache_dir+name_gel_atom)
		root = tree.getroot()

		# gets urls to images from post form
		for imgurl in root.iter('post'):
			url = imgurl.attrib.get('file_url')
			print(url)

			# gets picture file name
			f_url = url.replace(url[0:37],"")

			if download == True and os.path.exists(cache_dir+f_url) == False:
				# if file is already downloaded, it will skip it 
				urllib.request.urlretrieve(url,cache_dir+f_url)
				print(f_url)

class Danbooru(object):
	"""docstring for Danbooru"""
	def __init__(self, url="http://gelbooru.com/"):
		super(Danbooru, self).__init__()
		self.url = url

		def get_time():
			# datetime.datetime.now() method
			now = datetime.datetime.now()

			hour = datetime.time(now.hour)
			minute = datetime.time(now.minute)
			second = datetime.time(now.second)

			# isoformat() >> str method
			isotime = datetime.datetime.now().isoformat()

			s_iso = str(isotime)
			s_iso[0:9] = date

	def dan_jsonGET(url="http://gelbooru.com/",tag="loli",limit=100):
		# sends request to json API on danbooru and saves in variable 'json_r'
		json_g = urllib.request.urlopen(url+"posts.json?limit={0}?search[tags]={1}".format(str(limit), tag))
		json_r = json_g.read()

		# opens file following new filename format, and writes json data to it
		file_dan = open(cache_dir+"danbooru-"+date+"-T-"+str(hour)+"-"+str(minute)+"-"+str(second)+".json", "wb")	
		file_dan.write(json_r) 		

		"""Filename new format: 
		example: danbooru-2013-10-08-T-19-11-12.json
			1st place: Object name
			2nd place: Date in iso format
			3rd place: (starting with "-T-") Time: hour - minute - second
		"""

def execute_gel(take_limit=100):
	# auto get a page, and put into "gel.html" file
	Gelbooru("http://gelbooru.com/index.php?page=post&s=list&tags=loli")
	maigah = Gelbooru.gel_rssatom(by_tag_loli=True,limit=take_limit)

def execute_dan(take_limit=100):
	# calls dan_jsonGET -> saving 100 entries with tag "loli"
	# to file following format in Danbooru init()
	omgomg = Danbooru.dan_jsonGET(tag="loli",limit=take_limit)