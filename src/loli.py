#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import argparse
import loli_gelbooru
import loli_spam

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

str_a_limit = str(args.limit)

# Taking integer from args and call execute_gel() with it
print('Downloading: ' + str_a_limit +' latest loli pics from Gelbooru.\n','-'*80)
loli_gelbooru.execute_gel(take_limit=args.limit)
print('[+] Done with downloading latest ' + str_a_limit + 'loli pics from Gelbooru.') 

# execute_spam() (from loli_spam.py) call
print('Getting list of google results for keyword: '+args.keywords+'\n','-'*80)
loli_spam.execute_spam(keywords_f_f=args.keywords)
print('[+] Done with getting google results for "'+args.keywords+'" keywords.')
