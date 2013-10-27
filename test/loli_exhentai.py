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

