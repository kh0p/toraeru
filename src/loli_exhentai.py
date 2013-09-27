#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import loli_spam
import urllib.request
import http.cookiejar

loli_spam.execute()
cache_dir = "cache/"

def exhentai_try():
	# I need to came up with other idea
	# problem is with deleting cookies
	# -> getting rid of sadpanda stuff

	exhentai_home = urllib.request.urlopen("http://exhentai.org/",timeout=5)
	cj = http.cookiejar.CookieJar.clear(exhentai_home) # clears cookies of exhentai_site
	exhentai_site = urllib.request.urlopen("http://exhentai.org/g/456745/626c55332f/",cj,timeout=5)
	read_ex = exhentai_site.read()

	file_1 = open(cache_dir+"site.html","wb")
	file_1.write(read_ex)

def gel_open(url="http://gelbooru.com/"):
	gelbooru_loli = urllib.request.urlopen(url,timeout=5)
	read_gel_loli = gelbooru_loli.read()

	name_gel_loli = "gel.html"
	file_gel_loli = open(cache_dir+name_gel_loli,"wb")
	file_gel_loli.write(read_gel_loli)

gel_open("http://gelbooru.com/index.php?page=post&s=list&tags=loli")
