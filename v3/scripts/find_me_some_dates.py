#!/usr/bin/env python 
# -*- coding: utf8 -*-

import ssl, urllib, urllib.request, re, collections, pprint


def request():

urllib.





def find_me_some_dates(url):
	regex = b'[0-9]{4}'
	regex2 = b'.{4}[0-9]{4}.{4}'
	ignore_ssl_err = ssl._create_unverified_context()
	response = urllib.request.urlopen(url, context=ignore_ssl_err)
	html = response.read()
	match = re.findall(regex, html)
	match2 = re.findall(regex2, html)
	pprint.pprint(collections.Counter(match))
	#pprint.pprint(collections.Counter(match2))

find_me_some_dates(input('URL: '))

input()
