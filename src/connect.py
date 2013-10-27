#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import urllib.request
import json

cache_dir = "cache/"
def token_request(TOKEN_r=1):
	API_ID = "BG7YT2TDK7WDPI6IRQT8IHTHV7DIMNXI"
	
	if TOKEN_r == 1:
		TOKEN = urllib.request.urlopen("http://animeunlocked.com/token.php?key=$_GET['{0}']".format(API_ID))
		r_token = TOKEN.read()

		j_token = open(cache_dir+"token_1.json","wb")
		j_token.write(r_token)

	elif TOKEN_r == 2:
		TOKEN = urllib.request.urlopen("http://animeunlocked.com/token.php?key=$_GET['key']")
		r_token = TOKEN.read()

		j_token = open(cache_dir+"token_2.json","wb")
		j_token.write(r_token)

	
	else:
		pass


token_request(TOKEN_r=1)
token_request(TOKEN_r=2)

# Both test fails and returns:
#
#{"api":{"total":0,"current_page":""},
# "output":{"error_id":"api.unable_to_find_api_key",
# "error_message":"Unable to find API key."}}
