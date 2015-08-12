#!/usr/bin/env python 
# -*- coding: utf8 -*-

def referencer():
	author_company = input(r'Author/Company: ').strip()
	publish_date = input(r'Publication Date (Year, Mon Day): ').strip()
	article_title = input(r'Title: ').strip()
	url_page = input(r'URL: ' ).strip()
	print(author_company + '. (' + publish_date + '). ' + article_title + ' <' + url_page + '>' )


referencer()

input()
