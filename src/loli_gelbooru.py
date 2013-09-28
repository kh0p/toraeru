#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import loli_spam
import urllib.request
import http.cookiejar
import xml.etree.ElementTree as eltree

loli_spam.execute()
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
					by_tag_loli = False,limit = 100):
		"""gel_rssatom:

		by_tag_loli: 
			If you want to get feed for tag 'loli', you need to switch 
			by_tag_loli to True.
		limit: 
			limit is variable that stores maximum number of loli entries. 
			maximum number of entries that can be loaded is 100 (limited 
			by gelbooru API).
		"""

		if by_tag_loli == True:
			url = "http://gelbooru.com/index.php?page=dapi&s=post&q=index&limit={0}&tags=loli".format(limit)

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
		tree = eltree.parse(cache_dir+'atom.xml')
		root = tree.getroot()

		def get_image():
			img_url = root.findall("./post/[@file_url]")
			print(img_url)

# auto get a page, and put into "gel.html" file
Gelbooru("http://gelbooru.com/index.php?page=post&s=list&tags=loli")

Gelbooru.gel_rssatom(by_tag_loli=True)
Gelbooru.gel_rssatom.get_image()