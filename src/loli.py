#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import argparse
import pictures
import spam

"""
Arguments:
	limit -> int (ex. 1, 2, 10, 25)
		max. 100;
	keywords -> str (ex. loli, hentai, baka)
		no limit of keywords;
"""

# Creating ArgumentParser object
parser = argparse.ArgumentParser(description="Arguments for loli.py")

# Adding info about arguments for ArgumentParser
parser.add_argument('limit', metavar='N', type=int, nargs=1,
					help="Limit for gelbooru downloader.",
					default=25)
parser.add_argument('keywords', metavar='S', type=str, nargs="+",
					help="List of keywords to search on google.",
					default='lolicon loli pictures')
# Parse all arguments to args variable
args = parser.parse_args()

strLimit = ' '.join(str(e) for e in args.limit)
strKeys	 = ' '.join(str(e) for e in args.keywords)

# Taking integer from args and call execute_gel() with it
print('Downloading: '+strLimit+' latest loli pics from Gelbooru.\n','-'*78)
loli_gelbooru.execute_gel(take_limit=args.limit)
print('[+] Done with downloading latest '+strLimit +'loli pics from Gelbooru.') 

# execute_spam() (from loli_spam.py) call
print('Getting list of google results for keyword: '+strKeys+'\n','-'*78)
loli_spam.execute_spam(keywords_f_f=strKeys)
print('[+] Done with getting google results for "'+strKeys+'" keywords.')
